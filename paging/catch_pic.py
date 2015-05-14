#-*- coding:utf-8 -*-
import urllib2
import re 
import mysql
import sys

def catch(url):
    website=urllib2.urlopen(url)
    html=website.read()
    return html
print catch('http://www.1905.com/mdb/star/')
