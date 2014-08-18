# -*- coding: utf-8 -*-
import os
from markupsafe import Markup

__author__ = 'myth'
"""
css、js文件版本控制
"""


class Context(object):

    def __init__(self):

        self._source = {}

    @property
    def source(self):
        return self._source

    def css(self, path, domain=None, rel="stylesheet", charset="UTF-8", query=None, **kwargs):
        """
        css连接地址生成
        """

        link = """<link %s>"""

        link = self._link(link, path, 'href', domain=domain, query=query, rel=rel, charset=charset, **kwargs)
        return link

    def js(self, path, domain=None, charset="UTF-8", query=None, **kwargs):
        """
        js连接地址生成
        """

        link = """<script %s></script>"""
        link = self._link(link, path, 'src', domain=domain, query=query, charset=charset, **kwargs)
        return link

    def _link(self, link, path, href, domain=None, query=None, **kwargs):

        if not path:
            return ''
        version = self.source.get(path)
        if version:
            _path, suffix = self.splitext(path)
            path = '{0}.v{1}{2}'.format(_path, version, suffix)

        if query:
            path = '{0}?{1}'.format(path, query)
        if domain:
            if not (path.startswith('http://') or path.startswith('https://')):
                path = '{0}{1}'.format(domain, path)

        kwargs[href] = path

        link_str = self.gen_link(link, **kwargs)
        return Markup(link_str)

    def splitext(self, path):
        """
        检查css或者js路径分割
        :param path:
        :type path:
        """

        _path, suffix = os.path.splitext(path)
        return _path, suffix

    def gen_link(self, link, **kwargs):
        """
        生成连接地址
        """
        rows = list()
        for k, v in kwargs.iteritems():
            row = '{0}="{1}"'.format(k, v)
            rows.append(row)

        return link % ' '.join(rows)