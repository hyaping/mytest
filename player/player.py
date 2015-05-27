# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
import re
import pymysql
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import tornado.ioloop
import tornado.httpserver
import tornado.web
from mako.lookup import TemplateLookup

def get_player(url):                                                                 
    website=urllib2.urlopen(url)                                                     
    html=website.read()                                                              
    teamname=re.findall(r'''<span\s+class="team_name"><a\s+href="(.*)">(.*)</a></span>''',html)
    return teamname  

Base=declarative_base()
engine=create_engine('mysql+pymysql://root:@localhost:3306/db1?charset=utf8')
DBSession=sessionmaker(bind=engine)
session=DBSession()
class Ball(Base):
    __tablename__='ball'
    id=Column(Integer,primary_key=True)
    team_name=Column(String(255))
    name=Column(String(255))
    href=Column(String(255))
    size=Column(Integer)
    site=Column(String(255))
    height=Column(String(255))
    weight=Column(String(255))
    birthday=Column(String(255))
    contract=Column(String(255))

def get_all_users(session,offset=0,limit=10):
    all_users=session.query(Ball).offset(offset).limit(limit).all()
    return all_users

def get_all(session):
    return session.query(Ball).all()
def get_users(session):
    players=session.query(Ball.teamname).all()
    return players

def get_users_by_team(session,teamname,offset=0,limit=10):
    player_datas=session.query(Ball).filter(Ball.team_name==teamname).offset(offset).limit(limit).all()
    return player_datas
def get_total_by_team(session,teamname):
    total=session.query(Ball).filter(Ball.team_name==teamname)
    return total

def get_id_by_team(session,teamname):
    teamid=session.query(Ball.id).filter(Ball.team_name==teamname).first()
    return teamid

class Pager:
    def __init__(self, total_count,page_size=10,cur_page=1):
        self.total_count=total_count
        self.page_size=page_size or 10
        self.cur_page=cur_page if cur_page>0 else 1

    def get_record_index(self):
        return int(self.cur_page-1)*self.page_size

    def get_page_count(self):
        return int(int(self.total_count+self.page_size-1)/self.page_size)
 
    def getPage(self):
        _page_count=self.get_page_count()
        pageidxs=range(1,_page_count+1)
        return pageidxs

def renderweb(makol,**datas):
    tl=TemplateLookup(directories=['/home/dev/mytest/player'],
                      module_directory='/home/dev/mytest/player',output_encoding='utf-8')
    a=tl.get_template(makol)
    return a.render(**datas)

class PlayersHandler(tornado.web.RequestHandler):
    def get(self):
        players=get_player('http://g.hupu.com/nba/players/')
        team=self.get_argument('teams','')
        pageindex = int(self.get_argument("pageindex",1))
        page_size = 10
        if team:
            totals=get_total_by_team(session,team)
            print totals
            print type(totals)
            total_count = totals.count()
            page= Pager(total_count=total_count,page_size=page_size,cur_page=pageindex)
            player_datas=get_users_by_team(session,team,offset=page.get_record_index(),limit=page_size)
            pages=page.getPage()
        else:
            totals=get_all(session)
            total_count = len(totals)
            page= Pager(total_count=total_count,page_size=page_size,cur_page=pageindex)
            player_datas=get_all_users(session,offset=page.get_record_index(),limit=page_size)
            pages=page.getPage()
        webl=renderweb('player.html',players=players,player_datas=player_datas,team=team,cur_page=page.cur_page,_page_count=page.get_page_count(),pageidxs=pages)
        self.write(webl)

app=tornado.web.Application([(r'/players',PlayersHandler)])

if __name__=='__main__':
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8906)
    tornado.ioloop.IOLoop.instance().start()

