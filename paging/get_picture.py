# -*- coding: utf-8 -*-
import re  
import pymysql
import urllib2
import sys
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def get_pic(url):
    website=urllib2.urlopen(url)
    html=website.read()
    pics=re.findall(r'<a\s+href="(/mdb/star/\d+/)"\s+target="_blank">.*<img\s+src="(\S+)"\s+title="(.*)"\s+alt=.*>',html)
    return pics
#f=get_pic('http://www.1905.com/mdb/star/')
#print f

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
def get_user(session):
    users=session.query(Pics).all()
    return users

x=range(100)
for i in x[1:]:
    https="http://www.1905.com/mdb/star/m1p%d.html" %i
    pics=get_pic(https)
#    print pics
    for j in pics:
        new_pics=Pics(href=j[0],src=j[1],name=j[2])
        user_add(session,new_pics)    
