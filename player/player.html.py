# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1432281195.993895
_enable_loop = True
_template_filename = '/home/dev/mytest/player/player.html'
_template_uri = 'player.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pageidxs = context.get('pageidxs', UNDEFINED)
        player_datas = context.get('player_datas', UNDEFINED)
        cur_page = context.get('cur_page', UNDEFINED)
        players = context.get('players', UNDEFINED)
        team = context.get('team', UNDEFINED)
        _page_count = context.get('_page_count', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n    <head><title>\u5404\u961f\u7403\u661f</title></head>\n    <body>\n')
        for j in players:
            __M_writer(u"        <a href='/players?teams=")
            __M_writer(unicode(j[1]))
            __M_writer(u"'>&nbsp;")
            __M_writer(unicode(j[1]))
            __M_writer(u'&nbsp;</a>\n')
        __M_writer(u'        <div>\n')
        if cur_page!=1:
            __M_writer(u"            <a href='/players?teams=")
            __M_writer(unicode(team))
            __M_writer(u'&pageindex=')
            __M_writer(unicode(cur_page-1))
            __M_writer(u"'>&nbsp;\u4e0a\u4e00\u9875&nbsp;</a>\n")
        for pageidx in pageidxs:
            __M_writer(u"            <a href='/players?teams=")
            __M_writer(unicode(team))
            __M_writer(u'&pageindex=')
            __M_writer(unicode(pageidx))
            __M_writer(u"'>&nbsp;")
            __M_writer(unicode(pageidx))
            __M_writer(u'&nbsp;</a>\n')
        if cur_page!=_page_count:
            __M_writer(u"            <a href='/players?teams=")
            __M_writer(unicode(team))
            __M_writer(u'&pageindex=')
            __M_writer(unicode(cur_page+1))
            __M_writer(u"'>&nbsp;\u4e0b\u4e00\u9875&nbsp;</a>\n")
        __M_writer(u'        </div> \n        <table>\n            <tr>\n            <td>\u961f\u540d</td><td>\u59d3\u540d</td><td>\u53f7\u7801</td><td>\u4f4d\u7f6e</td><td>\u8eab\u9ad8</td>\n            <td>\u4f53\u91cd</td><td>\u751f\u65e5</td><td>\u5408\u540c</td>\n            </tr>\n')
        for i in player_datas:
            __M_writer(u'            <tr>\n            <td>')
            __M_writer(unicode(i.team_name))
            __M_writer(u"</td><td><a href='http://g.hupu.com/'")
            __M_writer(unicode(i.href))
            __M_writer(u'>')
            __M_writer(unicode(i.name))
            __M_writer(u'</a></td><td>')
            __M_writer(unicode(i.size))
            __M_writer(u'</td><td>')
            __M_writer(unicode(i.site))
            __M_writer(u'</td><td>')
            __M_writer(unicode(i.height))
            __M_writer(u'</td><td>')
            __M_writer(unicode(i.weight))
            __M_writer(u'</td><td>')
            __M_writer(unicode(i.birthday))
            __M_writer(u'</td><td>')
            __M_writer(unicode(i.contract))
            __M_writer(u'</td>\n            </tr>   \n')
        __M_writer(u'        </table>\n    </body>\n</html>            \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "26": 2, "27": 6, "28": 7, "29": 7, "30": 7, "31": 7, "32": 7, "33": 9, "34": 10, "35": 11, "36": 11, "37": 11, "38": 11, "39": 11, "40": 13, "41": 14, "42": 14, "43": 14, "44": 14, "45": 14, "46": 14, "47": 14, "48": 16, "49": 17, "50": 17, "51": 17, "52": 17, "53": 17, "54": 19, "55": 25, "56": 26, "57": 27, "58": 27, "59": 27, "60": 27, "61": 27, "62": 27, "63": 27, "64": 27, "65": 27, "66": 27, "67": 27, "68": 27, "69": 27, "70": 27, "71": 27, "72": 27, "73": 27, "74": 27, "75": 30, "81": 75}, "uri": "player.html", "filename": "/home/dev/mytest/player/player.html"}
__M_END_METADATA
"""
