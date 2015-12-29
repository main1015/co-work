# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Binary
from db import timestamp_mixin
from db.database import Base

__author__ = 'myth'

"""
用户类
"""


@timestamp_mixin
class User(Base):
    """
    用户表
    """

    __tablename__ = 'user'

    # user表自增主键
    id = Column(Integer, primary_key=True)

    # 用户登录名称(唯一，通过程序控制)
    username = Column(String(80), default='', nullable=False, doc=u"用户登录名称")

    # 用户邮箱(唯一，通过程序控制)
    email = Column(String(80), default='', nullable=False, doc=u"用户邮箱")

    # 用户昵称(唯一，通过程序控制)
    nickname = Column(String(80), default='', nullable=False, doc=u"用户昵称")

    # 用户密码
    password = Column(Binary, nullable=False, doc=u"用户密码")

    # password salt
    salt = Column(String(6), default='', nullable=False, doc=u"密码加盐随机数")

    # 用户头像
    avatar = Column(String(120), default='', nullable=False, doc=u"用户头像")

    # 身份证号码(唯一，通过程序控制)
    id_number = Column(String(32), default='', nullable=False, doc=u"身份证号码")


@timestamp_mixin
class UserEmployer(Base):
    """
    用户雇主表
    """

    __tablename__ = 'user_employer'

    # user_employer表自增主键
    id = Column(Integer, primary_key=True)

    # 是否离职
    is_resign = Column(Boolean, default=False, nullable=False, doc=u'是否离职')

    # 是否验证
    is_verify = Column(Boolean, default=False, nullable=False, doc=u'是否验证')

    # 用户表id
    user_id = Column(Integer, default=0, nullable=False, doc=u'用户表id， user表id')

    # 用户昵称
    nickname = Column(String(80), default='', nullable=False, doc=u"用户昵称")

    # 公司表id
    company_id = Column(Integer, default=0, nullable=False, doc=u'公司表id， company表id')

    # 公司名称
    company_name = Column(String(255), default='', nullable=False, doc=u"公司名称")

    # 职位
    position = Column(String(80), default='', nullable=False, doc=u"职位")

    # 部门
    department = Column(String(80), default='', nullable=False, doc=u"部门")

    # 入职时间
    entry_at = Column(DateTime, default='0000-00-00 00:00:00', nullable=False, doc=u'入职时间')

    # 离职时间
    dimission_at = Column(DateTime, default='0000-00-00 00:00:00', nullable=False, doc=u'离职时间')