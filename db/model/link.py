# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from sqlalchemy import Integer
from db import timestamp_mixin, status_mixin, Base

__author__ = 'myth'
"""
Created by myth on 15-12-25.
"""


@timestamp_mixin
@status_mixin
class Link(Base):
    """
    链接表
    """

    __tablename__ = 'link'

    # link表自增主键
    id = Column(Integer, primary_key=True)

    # 用户表id
    user_id = Column(Integer, default=0, nullable=False, doc=u'用户表id， user表id')

    # 标题
    title = Column(String(80), default='', nullable=False, doc=u"标题")

    # 内容
    content = Column(String(255), default='', nullable=False, doc=u"内容")

    # 图标
    icon = Column(String(255), default='', nullable=False, doc=u"图标")

    # 链接地址
    href = Column(String(255), default='', nullable=False, doc=u"链接地址")