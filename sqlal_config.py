# -*- coding=utf-8 -*-

import os
import sys
sys.path.append('.')
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
sqlal_env = os.environ.get('product','debug')
print 'sqlal_env:',sqlal_env
try:
    if sqlal_env == 'debug':
        MYSQL_CONFIG = dict(
            host = '192.168.1.249',
            port = 3307,
            user = 'beta',
            passwd = 'f0cf2a92516045024a0c99147b28f05b'
            )

        MYSQL_STAT_CONFIG = dict(
            host = '192.168.1.166',
            port = 3306,
            user = 'editor',
            passwd = 'x7PfEb9bor74oqpF9dE8IWB8p'
            )
    elif sqlal_env == 'beta':
        MYSQL_CONFIG = dict(
            host = '192.168.1.249',
            port = 3306,
            user = 'beta',
            passwd = 'f0cf2a92516045024a0c99147b28f05b'
            )
    elif sqlal_env == '':
        MYSQL_CONFIG = dict(
            host = '192.168.1.238',
            port = 3306,
            user = 'editor',
            passwd = 'x7PfEb9bor74oqpF9dE8IWB8p'
            )
except Exception,ex:
    print ex


def sqlal_model(database_name, pool_recycle):
    _sqlal_config = dict(
        host         = MYSQL_CONFIG['host'],
        port         = MYSQL_CONFIG['port'],
        user         = MYSQL_CONFIG['user'],
        passwd       = MYSQL_CONFIG['passwd'],
        database     = database_name,
        charset      = 'utf8',
    )
    connection_str = 'mysql+pymysql://%(user)s:%(passwd)s@%(host)s:%(port)d/%(database)s?charset=%(charset)s'  % _sqlal_config
    engine = create_engine(connection_str, echo = False, pool_recycle = pool_recycle)
    Session = scoped_session(sessionmaker(bind=engine,
                 extension=ZopeTransactionExtension(),expire_on_commit=False))    
    db_session = Session()
    return db_session
