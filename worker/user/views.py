# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, make_response, g, request
from forms.page import PageForm
from forms.user import UserRegisterForm, UserLoginForm, UserWorkExperienceForm
from util.forms import print_form
from util.strings import password_encrypt
from util.template import render
from worker.decorator import login_required, rjson
from worker.lib.cookie import set_user_login_cookie, delete_user_login_cookie
from db.service.user import add_user, find_email_user, find_user_work_experiences, add_user_work_experiences
from worker.result import ResultCode, Result

__author__ = 'myth'

"""
用户控制器
"""
user_page = Blueprint('user_page', __name__)


@user_page.route('/u/')
@login_required
def user_home_page():
    """
    用户主页
    """
    data = dict(tab=dict(user='active'))
    return render("/user/detail.html", **data)


@user_page.route('/u/register')
def user_register_page():
    """
    用户注册页面
    """
    data = {}
    form = UserRegisterForm()
    data['form'] = form
    return render("/user/register.html", **data)


@user_page.route('/u/register.post', methods=('POST',))
def user_register_post_page():
    """
    用户注册申请
    """
    data = {}
    form = UserRegisterForm()

    if form.validate():
        user = find_email_user(form.email.data)
        if user:
            form.email.errors.append(u'该邮箱已经注册，请输入其他邮箱！')
        else:
            user = add_user(form.email.data, form.password.data)
            to_redirect = redirect(url_for('user_page.user_home_page'))
            response = make_response(to_redirect)
            set_user_login_cookie(user.id, response)
            return response

    data['form'] = form
    return render("/user/register.html", **data)


@user_page.route("/u/login")
def user_login_page():
    """
    用户登录界面
    """
    data = {}
    form = UserLoginForm()

    data['form'] = form
    return render("/user/login.html", **data)


@user_page.route("/u/login", methods=("POST",))
def user_login_post_page():
    """
    用户登录认证
    """
    data = dict()
    form = UserLoginForm()
    if form.validate():
        user = find_email_user(form.email.data)
        if user:
            if user.password == password_encrypt(form.password.data, user.salt):
                to_redirect = redirect(url_for('user_page.user_home_page'))
                response = make_response(to_redirect)
                set_user_login_cookie(user.id, response)
                return response
            else:
                form.password.errors.append(u'密码错误！')
        else:
            form.email.errors.append(u'用户不存在！')

    data['form'] = form
    return render("/user/login.html", **data)


@user_page.route("/u/logout")
def user_logout_page():
    """
    用户退出
    """
    to_redirect = redirect(url_for('user_page.user_login_page'))
    response = make_response(to_redirect)
    delete_user_login_cookie(response)
    return response


@user_page.route("/u/work_experience")
@login_required
def user_work_experience_page():
    """
    用户的工作经历
    """

    data = {}
    user = g.curr_user
    page_form = PageForm()
    form = UserWorkExperienceForm()

    data['page_form'] = page_form
    data['form'] = form

    data['is_error'] = False

    works, pages = find_user_work_experiences(user, limit=page_form.l.data, page=page_form.p.data)
    if not works:
        data['is_error'] = True
    data['works'] = works
    data['pages'] = pages
    return render('/user/work.html', **data)


@user_page.route("/u/work_experience.post", methods=("POST",))
@login_required
def user_work_experience_post_page():
    """
    用户的工作经历
    """

    data = {}
    user = g.curr_user
    page_form = PageForm()
    form = UserWorkExperienceForm()

    data['page_form'] = page_form
    data['form'] = form

    data['is_error'] = False
    if form.validate():
        #如果提交成功就跳转到get请求上
        #防治用户通过F5刷新重复提交 Post-Redirect-Get (PRG)模式。
        work = add_user_work_experiences(user, form.company_name.data, form.position.data,
                                         form.entry_at.data, is_resign=form.is_resign.data,
                                         dimission_at=form.dimission_at.data,
                                         company_id=form.company_id.data)
        to_redirect = redirect(url_for('user_page.user_work_experience_page'))
        return to_redirect
    else:
        data['is_error'] = True

    works, pages = find_user_work_experiences(user, limit=page_form.l.data, page=page_form.p.data)
    data['works'] = works
    data['pages'] = pages
    return render('/user/work.html', **data)
