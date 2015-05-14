# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from mako.lookup import TemplateLookup
import tornado.ioloop
import tornado.httpserver
import pymysql
import sys
import tornado.web

Base=declarative_base()
engine=create_engine('mysql+pymysql://root:@localhost:3306/db1?charset=utf8')
DBSession=sessionmaker(bind=engine)
session=DBSession()
class Pics(Base):
    __tablename__='pics'
    id=Column(Integer,primary_key=True)
    href=Column(String(255))
    src=Column(String(255))
    name=Column(String(255))
def user_add(session,user):
    session.add(user)
    session.commit()
def get_users(session,offset=0,limit=20):
    users=session.query(Pics).offset(offset).limit(limit).all()
    return users

def get_users_count(session,pagesize = 20):
    result=session.query(func.count(Pics.id)).scalar()
    return result

def renderweb(makol,**datas):
    tl=TemplateLookup(directories=['/home/dev/mytest/paging'],module_directory='/home/dev/mytest/paging',output_encoding='utf-8')
    a=tl.get_template(makol)
    return a.render(**datas)
class Pager:
    def __init__(self,total_count,page_size=20,cur_page=1):
        self.url="&nbsp;<a href='/stars?pageindex={0}'>{1}</a>&nbsp;"
        self.total_count=total_count
        self.page_size=page_size or 20
        self.cur_page=cur_page if cur_page>0 else 1
        self.per_page_count = 10

    def get_record_index(self):
        return int(self.cur_page - 1) * self.page_size

    def get_page_count(self):
        return int(int(self.total_count + self.page_size - 1) / self.page_size)

    def getPage(self):
        _page_count = self.get_page_count()
        pageidxs = range(1,_page_count+1)
        idx_count = len(pageidxs)
        start_idx,end_idx = 1,self.per_page_count
        if idx_count > self.per_page_count:
            if self.cur_page>6:
                start_idx = self.cur_page - 5
                if self.cur_page<idx_count-4:
                    end_idx = self.cur_page + 4
                else:
                    end_idx = idx_count
                    start_idx = end_idx - 9
        page_idx_list = pageidxs[start_idx-1:end_idx] if pageidxs else []
        urls = []
        if self.cur_page!=1:
            urls.append(self.url.format(int(self.cur_page-1),"上一页"))
        for pageidx in page_idx_list:
            urls.append(self.url.format(pageidx,pageidx))
        if self.cur_page!=_page_count:
            urls.append(self.url.format(int(self.cur_page+1),"下一页"))
        return "".join(urls)

class Star_picsHandler(tornado.web.RequestHandler):
    def get(self):
        pageindex = int(self.get_argument("pageindex",1))
        page_size = 20
        total_count = get_users_count(session)
        page = Pager(total_count=total_count,page_size=page_size,cur_page=pageindex)
        result=get_users(session,offset = page.get_record_index(),limit = page_size)
        pages = page.getPage()
        self.write(renderweb('py_paging.html',ls = result,pages = pages))

app=tornado.web.Application([(r'/stars',Star_picsHandler)])

if __name__=='__main__':
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8901)
    tornado.ioloop.IOLoop.instance().start()
