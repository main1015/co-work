# -*- coding: utf-8 -*-
import datetime
from wtforms import DateField

__author__ = 'myth'


class _DateField(DateField):

    def process_formdata(self, valuelist):
        if valuelist:
            date_str = ' '.join(valuelist)
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).date()
            except ValueError:
                self.data = None