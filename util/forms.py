# -*- coding: utf-8 -*-
from wtforms import Field

__author__ = 'myth'


def print_form(form):
    """
    打印form对象
    :param form:
    """
    print '-'*80
    for name, field in form.__dict__.iteritems():

        if isinstance(field, Field):
            print "%s = %r %r" % (name, field.data, type(field.data))

    print '='*80