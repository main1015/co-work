# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, HiddenField, DateField, SelectField, ValidationError, StringField
from wtforms.validators import Required, EqualTo, Email, DataRequired
from forms import _Form
from forms._field import _DateField

__author__ = 'myth'


class UserRegisterForm(Form):
    """
    用户注册表单
    """

    email = StringField(u"邮件",  [
        DataRequired(message=u"邮件地址不能为空！"),
        Email(message=u"无效电子邮件地址!")
    ])
    password = PasswordField(u'密码', [
        DataRequired(message=u"密码不能为空！"),
        EqualTo('confirm', message=u'密码必须一致!')
    ])

    confirm = PasswordField(u'确认密码')


class UserLoginForm(Form):
    """
    用户登录表单
    """
    email = StringField(u"邮件", [
        DataRequired(message=u"邮件地址不能为空！"),
        Email(message=u"无效电子邮件地址!")
    ])
    password = PasswordField(u'密码', [
        DataRequired(message=u"密码不能为空！"),
    ])


class UserWorkExperienceForm(_Form):
    """
    用户工作经历表单
    """

    company_name = StringField(u"公司名称", [
        DataRequired(message=u"公司名称不能为空！")
    ])
    company_id = HiddenField(u"公司id")
    position = StringField(u"职位", [
        DataRequired(message=u"职位不能为空！")
    ])

    department = StringField(u"部门", [
        DataRequired(message=u"部门不能为空！")
    ])

    entry_at = DateField(u"入职日期", [
        DataRequired(message=u"入职日期不能为空！")
    ])

    dimission_at = _DateField(u"离职日期")

    is_resign = SelectField(u"是否离职", choices=[(0, u'否'), (1, u'是')], coerce=int,
                            default=(0, u'否'))

    def validate_dimission_at(self, field):
        if bool(self.is_resign.data) and field.data is None:
            raise ValidationError(field.gettext(u'离职日期不能为空'))
