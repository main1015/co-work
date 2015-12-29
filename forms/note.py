# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextAreaField, DecimalField, IntegerField, ValidationError, StringField
from wtforms.validators import DataRequired

__author__ = 'myth'


class NoteForm(Form):
    """
    笔记表单
    """
    title = StringField(u"标题", [
        DataRequired(message=u"标题不能为空！")
    ])

    content = TextAreaField(u"内容", [
        DataRequired(message=u"内容不能为空！")
    ])

    x = DecimalField(u'x', default=0)
    y = DecimalField(u'y', default=0)
    z = IntegerField(u'z', default=0)

    uid = IntegerField(u'user_id', default=0)

    def validate_x(self, field):
        min_x, max_x = 0, 650
        if not min_x <= field.data <= max_x:
            raise ValidationError(field.gettext(u'x坐标必须在%d～%d范围内！' % (min_x, max_x)))

    def validate_y(self, field):
        min_y, max_y = 0, 415
        if not min_y <= field.data <= max_y:
            raise ValidationError(field.gettext(u'y坐标必须在%d～%d范围内！' % (min_y, max_y)))

    def validate_z(self, field):
        min_z, max_z = 0, 99
        if not min_z <= field.data <= max_z:
            raise ValidationError(field.gettext(u'z坐标必须在%d～%d范围内！' % (min_z, max_z)))