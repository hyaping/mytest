# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1431596075.265625
_enable_loop = True
_template_filename = '/home/dev/mytest/landing/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <body>\n        <form  action=\'/login\' method=\'post\'>\n            <table width=\'100%\' height=\'100%\' border=\'0px\'>\n                <tr><td>\u59d3\u540d\uff1a</td><td><input type=\'text\' name=\'username\'/></td></tr>\n                <tr><td>Tel</td><td><input type=\'text\' name=\'tel\'/></td></tr>\n                <tr><td>\u5bc6\u7801\uff1a<input type=\'password\' name=\'passwd\'/></td></tr>\n                <tr><td>\u6027\u522b\uff1a</td><td><span>\u7537</span><input type=\'radio\' name=\'sex\' value=\'male\'/><span>\u5973</span><input type=\'radio\' name=\'sex\' value=\'female\'/></td></tr>\n                <tr><td><input type="submit">\u5b8c\u6210</td></tr>\n                \n            </table>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 20, "20": 2, "15": 0}, "uri": "login.html", "filename": "/home/dev/mytest/landing/login.html"}
__M_END_METADATA
"""
