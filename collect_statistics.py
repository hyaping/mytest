# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, DateTime
from sqlalchemy import func
from sqlal_config import sqlal_model
import time
import datetime
import transaction

Base = declarative_base()
class ThreadCollect(Base):
    '''
    帖子收藏
    '''
    __tablename__   = 'thread'
    __table_args__  = {'schema': 'collection'}

    id         = Column('id', Integer, primary_key=True)
    thread_id  = Column('thread_id', Integer)
    created_at = Column('created_at', DateTime)

class Threads(Base):
    __tablename__   = 'threads'
    __table_args__  = {'schema': 'forum'}

    id          = Column('id', Integer, primary_key=True)
    category_id = Column('category_id', Integer)

class Bankuai(Base):
    __tablename__   = 'bankuai'
    __table_args__  = {'schema': 'forum'}

    id = Column('id', Integer, primary_key=True)

class CollectStatistics(Base):
    __tablename__  = 'collect_statistics'
    __table_args__ = {'schema': 'statistics'}
    id = Column('id',Integer, primary_key=True)
    bankuai_id  = Column('category_id', Integer)
    ts          = Column('ts', DateTime) 
    num         = Column('num', Integer)   

def get_collect_total_count():
    col_session = sqlal_model('collection',60)
    forum_session = sqlal_model('forum', 60)
    stat_session = sqlal_model('statistics', 60)
    try:
        _start_ts, _end_ts = get_default_date()    
        ts_filter = ThreadCollect.created_at.between(_start_ts, _end_ts)
        bankuai_collects = col_session.query(ThreadCollect.thread_id,
                                        func.date_format(ThreadCollect.created_at,"%Y-%m-%d").label("ts")) \
                                        .filter(ts_filter).all()
        thread_ids = map(lambda x: x.thread_id, bankuai_collects)
        thread_infos = forum_session.query(Threads.id,Threads.category_id) \
                                          .filter(Threads.id.in_(thread_ids)).all()
        thread_dict = dict(map(lambda x: (x.id, x.category_id), thread_infos))
        transaction.commit()

        bankuai_ids = list(set(thread_dict.values()))
        bankuai_collects = map(lambda x: dict(bankuai_id = thread_dict.get(x[0], 0),ts = x[1],num = 1), bankuai_collects)
        ts_list = list(set(i['ts'] for i in bankuai_collects))
        ts_list = sorted(ts_list)
        bankuai_thread_infos = {i: filter(lambda x:x["bankuai_id"]==i, bankuai_collects) for i in bankuai_ids}
        bankuai_thread_infos = map((lambda x:{"bankuai_id": x, 
                                                     "ts": i,
                                                    "num": reduce(lambda a,b: a+b,map(lambda x:x["num"],
                                                               filter(lambda y:y["ts"]==i,bankuai_thread_infos[x])) or [0])} for i in ts_list),\
                                    bankuai_thread_infos)
        _collect_statistics = CollectStatistics()
        _collect_statistics_list = []
        for thread_info in bankuai_thread_infos:
            _collect_statistics.bankuai_id  = thread_info["bankuai_id"]
            _collect_statistics.ts          = thread_info["ts"]
            _collect_statistics.num         = thread_info["num"]
            _collect_statistics_list.append(_collect_statistics)
        result = stat_session.add_all(_collect_statistics_list)
        transaction.commit()
        return result
    except Exception,ex:
        raise ex

def get_pre_date(pre_days=0):
    _now_date = datetime.date.today()
    _pre_date = _now_date - datetime.timedelta(days=pre_days)
    _str_pre_date = _pre_date.strftime('%Y-%m-%d')
    return _str_pre_date

def get_default_date():
    '得到默认查询日期'
    start = get_pre_date(7)
    end   = get_pre_date(1)
    return start, end

if __name__ == "__main__":
    get_collect_total_count()
