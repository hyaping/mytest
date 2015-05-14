# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431576090.683475
_enable_loop = True
_template_filename = '/home/dev/mytest/paging/stars.html'
_template_uri = 'stars.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        page_idx_list = context.get('page_idx_list', UNDEFINED)
        cur_page = context.get('cur_page', UNDEFINED)
        ls = context.get('ls', UNDEFINED)
        _page_count = context.get('_page_count', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <head><title>\u660e\u661f\u56fe\u5c55\u793a</title></head>\n    <body>\n')
        for i in ls:
            __M_writer(u'        <a href="http://www.1905.com')
            __M_writer(unicode(i.href))
            __M_writer(u'" rtarget="_blank">\n          <img src="')
            __M_writer(unicode(i.src))
            __M_writer(u'" width=75 heigh=100 hspace=20 vspace=20 alian=bottom></a>\n        <a href=\'http://www.1905.com')
            __M_writer(unicode(i.href))
            __M_writer(u"'>")
            __M_writer(unicode(i.name))
            __M_writer(u'</a>\n')
        __M_writer(u'        <div>\n')
        if cur_page!=1:
            __M_writer(u'             <a href="/stars?pageindex=')
            __M_writer(unicode(cur_page-1))
            __M_writer(u'">pageup</a>\n')
        for pageidx in page_idx_list:
            __M_writer(u'                <a href="/stars?pageindex=')
            __M_writer(unicode(pageidx))
            __M_writer(u'">')
            __M_writer(unicode(pageidx))
            __M_writer(u'</a>\n')
        if cur_page!=_page_count:
            __M_writer(u'                <a href="/stars?pageindex=')
            __M_writer(unicode(cur_page+1))
            __M_writer(u'">pagedown</a>\n')
        __M_writer(u'        </div>\n    <body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "24": 2, "25": 6, "26": 7, "27": 7, "28": 7, "29": 8, "30": 8, "31": 9, "32": 9, "33": 9, "34": 9, "35": 11, "36": 12, "37": 13, "38": 13, "39": 13, "40": 15, "41": 16, "42": 16, "43": 16, "44": 16, "45": 16, "46": 18, "47": 19, "48": 19, "49": 19, "50": 21, "56": 50}, "uri": "stars.html", "filename": "/home/dev/mytest/paging/stars.html"}
__M_END_METADATA
"""
