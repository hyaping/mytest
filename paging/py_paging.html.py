# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431513473.612325
_enable_loop = True
_template_filename = '/home/dev/mytest/paging/py_paging.html'
_template_uri = 'py_paging.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ls = context.get('ls', UNDEFINED)
        pages = context.get('pages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <head><title>\u660e\u661f\u56fe\u5c55\u793a</title>\n    <body>\n')
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
        __M_writer(u'        <div>')
        __M_writer(unicode(pages))
        __M_writer(u'</div>\n    <body>\n    </head>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 9, "33": 11, "34": 11, "35": 11, "41": 35, "15": 0, "22": 2, "23": 6, "24": 7, "25": 7, "26": 7, "27": 8, "28": 8, "29": 9, "30": 9, "31": 9}, "uri": "py_paging.html", "filename": "/home/dev/mytest/paging/py_paging.html"}
__M_END_METADATA
"""
