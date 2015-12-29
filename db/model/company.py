# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, Binary
from db import Base, timestamp_mixin

__author__ = 'myth'


"""
公司类
"""


@timestamp_mixin
class Company(Base):
    """
    公司表
    """

    __tablename__ = 'company'

    # company表自增主键
    id = Column(Integer, primary_key=True)

    # 公司全称(唯一，通过程序控制)
    full_name = Column(String(255), default='', nullable=False, doc=u"公司全称")
    # 公司简称
    short_name = Column(String(255), default='', nullable=False, doc=u"公司简称")

    # 公司邮箱(唯一，通过程序控制)
    email = Column(String(80), default='', nullable=False, doc=u"公司邮箱")

    # 用户密码
    password = Column(Binary, nullable=False, doc=u"用户密码")

    # password salt
    salt = Column(String(6), default='', nullable=False, doc=u"密码加盐随机数")

    # 用户头像
    avatar = Column(String(120), default='', nullable=False, doc=u"公司头像")

    # 公司网站地址
    website = Column(String(255), default='', nullable=False, doc=u"公司网站地址")

    # 公司年数
    age = Column(Integer, default=0, nullable=False, doc=u'公司年数')

    # 公司创建时间
    found_at = Column(DateTime, default='0000-00-00 00:00:00', nullable=False, doc=u'公司创建时间')