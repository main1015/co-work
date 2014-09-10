# -*- coding: utf-8 -*-
from sqlalchemy import func
from db.database import db_session
from db.model import Company
from db.service.db_util import inquiry_process

__author__ = 'myth'


def get_company_list(like_name, limit=10, page=1):
    """
    获取公司列表
    """
    condition = []
    if like_name:
        likes = [n for n in like_name]
        _like = '%%'.join(likes)
        _like = '%%%%%s%%%%' % _like
        condition.append(Company.full_name.like(_like))

    companies_query = Company.query
    count_query = db_session.query(func.count(Company.id))

    if condition:
        companies_query = companies_query.filter(*condition)
        count_query = count_query.filter(*condition)
    companies, pages = inquiry_process(count_query, companies_query, limit=limit, page=page)
    return companies, pages