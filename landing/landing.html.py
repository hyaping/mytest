# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431596111.305681
_enable_loop = True
_template_filename = '/home/dev/mytest/landing/landing.html'
_template_uri = 'landing.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <body>\n        <form name=\'input\' action=\'/landing\' method=\'post\'>\n                <tr><td>\u7528\u6237\u540d\uff1a</td><td><input type=\'text\' name=\'username\'/></td></tr>\n                <tr><td>\u5bc6\u7801\uff1a</td><td><input  type=\'password\' name=\'passwd\'/></td></tr>\n                <tr><td colspan=\'2\'>\n                <tr><td><input type="submit"/>\u767b\u9646</td><td></tr>\n                <a href=\'/login\'>\u6ce8\u518c</a>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 2, "15": 0}, "uri": "landing.html", "filename": "/home/dev/mytest/landing/landing.html"}
__M_END_METADATA
"""
