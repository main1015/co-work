# -*- coding: utf-8 -*-
from sqlalchemy import Column, SMALLINT, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declared_attr, declarative_base, DeclarativeMeta

__author__ = 'myth'


def repr_alchemy(alchemy):
    """
    __repr__返回的数据

    """

    repr = '<%r(' % alchemy.__class__.__name__
    columns = []
    if isinstance(alchemy.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        for c in alchemy.__table__.columns:
            value = getattr(alchemy, c.name)
            columns.append('%r=%r' % (c.name, value))
    return repr + ', '.join(columns) + ')>'


class _Base(object):
    """
    Custom sqlalchemy base model.
    """

    @classmethod
    def get(cls, id):
        """
        Get object by it's id.
        """

        return cls.query.get(id)

    @classmethod
    def get_multi(cls, ids):
        """
        Get objects by id list.
        """

        ids = {}.fromkeys(ids).keys()
        if len(ids) > 0:
            res = cls.query.filter(cls.id.in_(ids))
        else:
            res = []

        return dict((r.id, r) for r in res)

    @declared_attr
    def __tablename__(cls):
        """
        Automatic cover model map tablename to lower
        """

        return cls.__name__.lower()

    def __repr__(self):
        return repr_alchemy(self)

    # Default table config.
    __table_args__ = {'mysql_charset': 'utf8',
                      'mysql_engine': 'InnoDB'}


Base = declarative_base(cls=_Base)


def priority_mixin(cls):
    """
    Model column pri mixin decorator.
    """

    cls.priority = Column(SMALLINT, default=0, nullable=False)
    return cls


def status_mixin(cls):
    """
    Model column:status mixin decorator.
    """

    cls.is_banned = Column(Boolean, default=False, nullable=False)
    cls.is_deleted = Column(Boolean, default=False, nullable=False)
    return cls


def timestamp_mixin(cls):
    """
    Model column: timestamp mixin decorator.
    """

    cls.created_at = Column(DateTime, default=func.now(), nullable=False)
    cls.updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    return cls
