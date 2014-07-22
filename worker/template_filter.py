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
    return value.strftime(format)


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
