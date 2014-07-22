# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import func
from util.strings import random_str, password_encrypt
from db.database import db_session
from db.model import User, UserEmployer
from db.service.db_util import inquiry_process


__author__ = 'myth'


def add_user(email, password):
    """
    添加用户
    """
    user = User()
    user.email = email
    user.salt = random_str(6)
    user.password = password_encrypt(password, user.salt)
    db_session.add(user)
    db_session.commit()
    return user


def find_email_user(email):
    """
    根据用户邮箱查找用户
    """
    user = User.query.filter(User.email == email).first()
    return user


def find_user_work_experiences(user, limit=10, page=1):
    """
    获取用户的工作经历
    """

    condition = [UserEmployer.user_id == user.id]
    employers_query = UserEmployer.query
    count_query = db_session.query(func.count(UserEmployer.id))

    employers_query = employers_query.filter(*condition)
    count_query = count_query.filter(*condition)
    employers, pages = inquiry_process(count_query, employers_query, limit=limit, page=page)
    return employers, pages


def add_user_work_experiences(user, company_name, position, entry_at, is_resign=False, dimission_at=None, company_id=0):
    """
    添加用户工作经历
    """

    employer = UserEmployer()
    employer.user_id = user.id
    employer.nickname = user.nickname or user.email
    employer.company_name = company_name
    employer.company_id = company_id
    employer.position = position
    employer.entry_at = entry_at
    employer.is_resign = is_resign
    if is_resign:
        employer.dimission_at = dimission_at
    else:
        #解决sqlite不能插入默认字符串时间
        employer.dimission_at = entry_at
    db_session.add(employer)
    db_session.commit()
    return employer
