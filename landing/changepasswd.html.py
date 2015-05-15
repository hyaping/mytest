# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431658876.243657
_enable_loop = True
_template_filename = '/home/dev/mytest/landing/changepasswd.html'
_template_uri = 'changepasswd.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <body>\n        <form name=\'input\' action=\'/changepasswd\' method=\'post\'>\n                <tr><td>\u7528\u6237\u540d\uff1a</td><td><input type=\'text\' name=\'username\'/></td></tr>\n                <tr><td>\u539f\u5bc6\u7801\uff1a</td><td><input  type=\'password\' name=\'upasswd\'/></td></tr>\n\n                <tr><td>\u65b0\u5bc6\u7801\uff1a</td><td><input  type=\'password\' name=\'npasswd\'/></td></tr>\n                <tr><td colspan=\'2\'>\n                <tr><td><input type="submit">\u4fee\u6539\u6210\u529f</td></tr>\n        </form>\n    </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 2, "15": 0}, "uri": "changepasswd.html", "filename": "/home/dev/mytest/landing/changepasswd.html"}
__M_END_METADATA
"""
