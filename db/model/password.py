# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Column, String
from db import timestamp_mixin, Base

__author__ = 'myth'
"""
Created by myth on 15-12-22.
"""
"""
密码类
"""


@timestamp_mixin
class Password(Base):
    """
    密码类
    """

    __tablename__ = 'password'

    # password表自增主键
    id = Column(Integer, primary_key=True)

    # 标题
    title = Column(String(80), default='', nullable=False, doc=u"标题")

    # 内容
    content = Column(String(255), default='', nullable=False, doc=u"内容")

    # 属主
    user_id = Column(Integer, default=0, nullable=False, doc=u'用户表id， user表id')