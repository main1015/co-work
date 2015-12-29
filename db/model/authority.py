# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, SMALLINT
from db import Base, timestamp_mixin

__author__ = 'myth'
"""
权限
"""


@timestamp_mixin
class Role(Base):
    """
    角色表
    """

    __tablename__ = 'role'

    # role表自增主键
    id = Column(Integer, primary_key=True)

    # 角色名称
    name = Column(String(80), default='', nullable=False, doc=u"角色名称")

    # mode
    mode = Column(SMALLINT, default=0, nullable=False, doc=u'模式值')

    # 角色描述
    description = Column(Text, default='', nullable=False, doc=u'角色描述')


@timestamp_mixin
class Authority(Base):
    """
    权限表
    """

    __tablename__ = 'authority'

    # authority表自增主键
    id = Column(Integer, primary_key=True)

    # 权限名称
    name = Column(String(80), default='', nullable=False, doc=u"权限名称")

    # mode
    mode = Column(SMALLINT, default=0, nullable=False, doc=u'模式值')

    # 权限描述
    description = Column(Text, default='', nullable=False, doc=u'权限描述')


