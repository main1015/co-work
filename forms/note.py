# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, DecimalField, IntegerField, ValidationError
from wtforms.validators import Required

__author__ = 'myth'


class NoteForm(Form):
    """
    笔记表单
    """
    title = TextField(u"标题", [
        Required(message=u"标题不能为空！")
    ])

    content = TextAreaField(u"内容", [
        Required(message=u"内容不能为空！")
    ])

    x = DecimalField(u'x', default=0)
    y = DecimalField(u'y', default=0)
    z = IntegerField(u'z', default=0)

    uid = IntegerField(u'user_id', default=0)

    def validate_x(self, field):
        if not 0 <= field.data <= 650:
            raise ValidationError(field.gettext(u'x坐标必须在0～650范围内！'))

    def validate_y(self, field):
        if not 0 <= field.data <= 415:
            raise ValidationError(field.gettext(u'y坐标必须在0～415范围内！'))

    def validate_z(self, field):
        if not 0 <= field.data <= 99:
            raise ValidationError(field.gettext(u'z坐标必须在0～99范围内！'))