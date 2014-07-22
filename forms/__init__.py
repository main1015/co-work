# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms.compat import iteritems
__author__ = 'myth'


class _Form(Form):
    """
    base form
    """

    def validate(self, filter=[], extra_validators=None, isParent=False):

        if isParent:
            return super(Form, self).validate()

        self._errors = None
        success = True
        if callable(getattr(self, "_validate", None)):
            _fields = self._validate()
        else:
            _fields = self._fields
        for name, field in iteritems(_fields):
            if name in filter or field in filter:
                continue

            if extra_validators is not None and name in extra_validators:
                extra = extra_validators[name]
            else:
                extra = list()
            inline = getattr(self.__class__, 'validate_%s' % name, None)

            if inline is not None:
                extra.append(inline)

            if not field.validate(self, extra):
                success = False
        return success