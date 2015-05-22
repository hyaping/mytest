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
    teams=re.findall(r'''<span\s+class="team_name"><a\s+href="(.*)">(.*)</a></span>''',html)
    return teams
players=get_player('http://g.hupu.com/nba/players/')

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
def user_add(session,user):
    session.add(user)
    session.commit()

for i in players:
    website=urllib2.urlopen('http://g.hupu.com/'+i[0])
    html=website.read()
    player_datas=re.findall(r'<a\s+target="_blank"\s+href="(.*)">(.*)</a></b><p>.*</b></p></td>\s+<td>(\d+)</td>\s+<td>(.*)</td>\s+<td>(.*)</td>\s+<td>(.*)</td>\s+<td>(.*)</td>\s+<td\s+class="left">(.*)</b></td>',html)
    for j in player_datas:
        new_user=Ball(team_name=i[1],href=j[0],name=j[1],size=j[2],site=j[3],height=j[4],weight=j[5],birthday=j[6],contract=j[7])
        user_add(session,new_user)    

