# -*- coding: utf-8 -*-
import datetime
import ujson as json
from jinja2 import environmentfilter
from jinja2.filters import make_attrgetter


__author__ = 'myth'


def register_filter(jinja2_env):
    """
    Register jinja2 templte filter.
    """

    jinja2_env.filters['split'] = jinja2_split
    jinja2_env.filters['datetimeformat'] = datetimeformat
    jinja2_env.filters['isum'] = count_sum
    jinja2_env.filters['iattr'] = get_attr
    jinja2_env.filters['to_json'] = to_json
    jinja2_env.filters['to_days'] = to_days
    jinja2_env.filters['to_years'] = to_years


def to_json(value):
    try:
        result = json.dumps(value)
    except Exception, e:
        result = {}
    return result


def jinja2_split(value, sep):
    if value and isinstance(value, (str, unicode)):
        s = value.split(sep)
        return s
    else:
        return value


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    if not value:
        value = datetime.datetime.now()
    if isinstance(format, unicode):
        format = format.encode('utf-8')
    _value = value.strftime(format)
    return _value.decode('utf-8')


def to_days(start, end=None):
    """
    获取两个时间段的天数
    """
    if end is None:
        end = datetime.datetime.now()
    d = end - start
    return d.days


def to_years(days):
    """
    天数转换为年
    """
    year = days / 365
    _year = days / 365.
    if _year > year:
        years = (year, '+')
    else:
        years = (year, '')
    return u'%s%s' % years


@environmentfilter
def count_sum(environment, iterable, attribute=None, start=0):
    """
    类是jinja2中的sum过滤器
    :param iterable:
    :param attribute:
    :param start:
    :return:
    """
    if attribute is not None:
        func = make_attrgetter(environment, attribute)
        iterable = map(func, iterable)
    iterable = filter(None, iterable)
    return sum(iterable, start)


@environmentfilter
def get_attr(environment, value, attribute, default=None):
    """
    获取值，
    :param value:
    :param attribute:
    :param default:
    :return:
    """

    if value:
        func = make_attrgetter(environment, attribute)
        result = func(value)
    else:
        result = default
    return result
