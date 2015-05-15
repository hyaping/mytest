# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431596063.656621
_enable_loop = True
_template_filename = '/home/dev/mytest/landing/webl.txt'
_template_uri = 'webl.txt'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        ls = context.get('ls', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u"<head>\n<title>\u660e\u661f\u56fe</title>\n<body>\n    <p><a href='/changepasswd'>\u4fee\u6539\u5bc6\u7801</a></p>\n")
        for i in ls:
            __M_writer(u'        <a>\n         <img src="')
            __M_writer(unicode(i.img_url))
            __M_writer(u'" width=75 heigh=100 hspace=20 vspace=20 alian=bottom>  \n        </a>\n        <a href=\'/delete?ids=')
            __M_writer(unicode(i.id))
            __M_writer(u"'>")
            __M_writer(unicode(i.name))
            __M_writer(u'</a>\n')
        __M_writer(u'<body>\n</head>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"36": 30, "15": 0, "21": 2, "22": 6, "23": 7, "24": 8, "25": 8, "26": 10, "27": 10, "28": 10, "29": 10, "30": 12}, "uri": "webl.txt", "filename": "/home/dev/mytest/landing/webl.txt"}
__M_END_METADATA
"""
