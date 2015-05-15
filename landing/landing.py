#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from mako.lookup import TemplateLookup
import tornado.ioloop
import tornado.httpserver
import pymysql
import sys
import tornado.web
from dbhelper import DBHelper
Base=declarative_base()
engine=create_engine('mysql+pymysql://root:@localhost:3306/db1?charset=utf8')  #echo是可以显示数据表详情的
DBSession=sessionmaker(bind=engine)
session=DBSession()

class User(Base):
    __tablename__='tweb'
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    img_url=Column(String(20))
    page_url=Column(String(20))

class Users(Base):
    __tablename__='USERS'
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    password=Column(String(20))

def user_add(session,user):
    session.add(user)
    session.commit()
def get_user_by_name(session,name):
    try:
        user=session.query(Users.name).filter(Users.name==name).one()
    except:
        user=''   
    return user
def get_user_by_password(session,password):
    try:
        user=session.query(Users.password).filter(Users.password==password).one()
    except:
        user=''   
    return user

def get_users(session):
    users=session.query(User).all()
    return users
def update_user(name,password):
    user = session.query(Users).filter(Users.name==name).first()
    user.password=password
    print user.password
    session.add(user)
    session.commit()
    

def renderweb(makol,datas):
    tl=TemplateLookup(directories=['/home/dev/mytest/landing'],
        module_directory='/home/dev/mytest/landing',
        output_encoding='utf-8')
    a=tl.get_template(makol)
    #data=putout('','tweb',datas)
    return a.render(ls=datas)
class selectHandler(tornado.web.RequestHandler):
    def get(self):
        session = DBSession()
        result = get_users(session)
        self.write(renderweb('webl.txt',result))
    def post(self):
        self.redirect('/changepasswd')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(renderweb('login.html',''))
    def post(self):
        talk1=self.get_argument('username')
        talk1=str(talk1)
        if talk1:
            talk11=get_user_by_name(session,talk1)
            if talk11:
                self.redirect('/login')
            talk2=self.get_argument('passwd')
            new_user=Users(name=talk1,password=talk2)
            user_add(session,new_user)
            self.redirect('/landing')
        else:
            self.redirect('/login')

class LandingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(renderweb('landing.html',''))
    def post(self):
        namel=self.get_argument('username')
        passwdl=self.get_argument('passwd')
        print namel
        print passwdl
        name=get_user_by_name(session,namel)
        passwd=get_user_by_password(session,passwdl)
        print name
        print passwd
        if name:
            if passwd:
                self.redirect('/select')
            else:
                self.redirect('/login')
        else:
            self.redirect('/login')
class ChangepasswdHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(renderweb('changepasswd.html',''))
    def post(self):
        name=self.get_argument('username') 
        passing=self.get_argument('npasswd')
        print passing
        if passing:
            update_user(name,passing)
            self.redirect('/landing')
        self.redirect('/changepasswd')

app=tornado.web.Application([(r'/landing',LandingHandler),
                            (r'/login',LoginHandler),
                            (r'/select',selectHandler),
                            (r'/changepasswd',ChangepasswdHandler)])
if __name__=='__main__':
   # application.listen(8900)
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8900)
    tornado.ioloop.IOLoop.instance().start()

