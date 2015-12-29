# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DECIMAL, SMALLINT
from db import Base, timestamp_mixin, status_mixin

__author__ = 'myth'


@timestamp_mixin
@status_mixin
class Note(Base):
    """
    笔记表
    """

    __tablename__ = 'note'

    # note表自增主键
    id = Column(Integer, primary_key=True)

    # 用户表id
    user_id = Column(Integer, default=0, nullable=False, doc=u'用户表id， user表id')

    # 用户昵称
    nickname = Column(String(80), default='', nullable=False, doc=u"用户昵称")

    # 标题
    title = Column(String(80), default='', nullable=False, doc=u"标题")

    # 内容
    content = Column(String(255), default='', nullable=False, doc=u"内容")

    # 编辑人id
    editor_id = Column(Integer, default=0, nullable=False, doc=u'编辑人id， user表id')

    # 编辑人昵称
    editor_nickname = Column(String(80), default='', nullable=False, doc=u"编辑人昵称")

    x = Column(DECIMAL(6, 2), default=0, nullable=False, doc=u'x轴坐标')
    y = Column(DECIMAL(6, 2), default=0, nullable=False, doc=u'y轴坐标')
    z = Column(SMALLINT, default=0, nullable=False, doc=u'z轴坐标')

    @property
    def X(self):
        return int(self.x)

    @property
    def Y(self):
        return int(self.y)
