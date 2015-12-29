# -*- coding: utf-8 -*-
import os
from markupsafe import Markup
try:
    #need ordereddict
    from ordereddict import OrderedDict
except ImportError, e:
    try:
        from collections import OrderedDict
    except ImportError, e:
        OrderedDict = dict

__author__ = 'myth'
"""
css、js文件版本控制
"""


class Context(object):

    _css = dict()
    _js = dict()

    def __init__(self, source=None):

        self._source = source or dict()

    @classmethod
    def clean(cls):
        cls._css = dict()
        cls._js = dict()

    @property
    def source(self):
        return self._source

    def css(self, path, repeat=False, domain=None, rel=u"stylesheet", charset=u"UTF-8", query=None, **kwargs):
        """
        css连接地址生成
        :param path:
        :param repeat: 是否重新写入
        :param domain:
        :param rel:
        :param charset:
        :param query:
        :param kwargs:
        """
        if not repeat and path in self._css:
            return u''
        self._css[path] = self._css.get(path, 0) + 1

        link = u"""<link %s>"""

        link = self._link(link, path, u'href', domain=domain, query=query, rel=rel, charset=charset, **kwargs)
        return link

    def js(self, path, repeat=False, domain=None, charset="UTF-8", query=None, **kwargs):
        """
        js连接地址生成
        :param path:
        :param repeat: 是否重新写入
        :param domain:
        :param charset:
        :param query:
        :param kwargs:
        """

        if not repeat and path in self._js:
            return u''
        self._js[path] = self._js.get(path, 0) + 1

        link = u"""<script %s></script>"""
        link = self._link(link, path, u'src', domain=domain, query=query, charset=charset, **kwargs)
        return link

    def img(self, path, domain=None, query=None, **kwargs):
        """
        img标签
        """
        link = u"""<img %s />"""
        link = self._link(link, path, u'src', domain=domain, query=query, **kwargs)
        return link

    def _link(self, link, path, href, domain=None, query=None, **kwargs):

        if not path:
            return u''

        if 'version' in kwargs:
            version = kwargs.pop('version')
        else:
            version = None
        _path = self.source.get(path, version)
        if _path:
            path = _path
        # version = self.source.get(path)
        # if version:
        #     _path, suffix = self.splitext(path)
        #     path = u'{0}.v{1}{2}'.format(_path, version, suffix)

        if query:
            path = u'{0}?{1}'.format(path, query)
        if domain:
            if not (path.startswith(u'http://') or path.startswith(u'https://')):
                path = u'{0}{1}'.format(domain, path)

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
            row = u'{0}="{1}"'.format(k, v)
            rows.append(row)

        return link % ' '.join(rows)


class Source(object):

    def __init__(self, config=None, domain=None):
        self._source = dict()
        self.domain = domain

        if config and isinstance(config, dict):
            for k, v in config.iteritems():
                self[k] = v

    def __setitem__(self, key, value):

        if key in self._source:
            raise KeyError(u"资源中已经存在 %s!" % key)
        if isinstance(value, basestring):
            row = self._row(value)
        elif isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError(u"%s 资源格式错误!" % key)
            row = self._row(*value[::-1])
        elif isinstance(value, list):
            row = self._rows()
            for v in value:
                if len(v) != 2:
                    raise ValueError(u"%s 多版本资源格式错误!" % key)
                _row = self._row(*v[::-1])

                row[v] = _row

        self._source[key] = row

    def __getitem__(self, item):
        return self._source[item]

    def get(self, item, version=None):
        row = self._source.get(item, None)
        if row:
            if version:
                row = row.get(version, None)
            else:
                row = row.get_last()
        return row

    def _bind_domain(self, path):
        if self.domain:
            if not (path.startswith(u'http://') or path.startswith(u'https://')):
                path = u'{0}{1}'.format(self.domain, path)
        return path

    def __repr__(self):
        return str(self._source)

    class _row(object):

        def __init__(self, path, version='v0'):
            if not isinstance(path, basestring):
                raise ValueError(u'资源路径格式错误！')
            self.path = path
            self.version = version

        def __repr__(self):
            return u'{path: "%s", version: "%s"}' % (self.path, self.version)

        def get(self, version, d=None):
            if version == self.version:
                return self.path
            else:
                return d

        def get_last(self):
            return self.path

    class _rows(object):

        def __init__(self):
            self.rows = list()
            self._rows = dict()

        def __setitem__(self, key, value):
            self._rows[key] = value
            if not key in self.rows:
                self.rows.append(key)

        def __getitem__(self, item):
            return self._rows[item]

        def get(self, key, d=None):
            if key in self._rows:
                return self._rows[key].get_last()
            return d

        def __iter__(self):
            return iter(self.rows)

        def __len__(self):
            return len(self._rows)

        def __contains__(self, item):

            return item in self._rows

        def iteritems(self):
            for k in self.rows:
                v = self._rows[k]
                yield k, v

        def get_last(self):
            if len(self.rows):
                key = self.rows[0]
                return self._rows[key].get_last()
            return None


if __name__ == '__main__':

    s = Source({
        'a': ('v12', 'cdadsf'),
        'b': ('v12', 'cdadsf'),
        'c': ('v12', 'cdadsf'),
        'd': ('v12', 'cdadsf'),
        'e': [
            ('v2.3', '1dsasdf1'),
            ('v2.4', '2dsasdf2'),
            ('v2.7', '3dsasdf5'),
            ('v2.15', '4dsasdf3'),
            ('v2.6', '5dsasdf4'),
        ]
    })

    print 'a', s.get('a', 'v12')
    print 'a1', s.get('a')
    print 'e', s.get('e', 'v2.3')
    print 'e', s.get('e')



