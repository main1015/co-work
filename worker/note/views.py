# -*- coding: utf-8 -*-
from flask import Blueprint, g, redirect, url_for, request
from db.model import User
from db.service.note import add_note, get_user_recent_notes
from forms.note import NoteForm
from util.template import render
from worker.decorator import login_required

__author__ = 'myth'

note_page = Blueprint('note_page', __name__)


@note_page.route("/note/index")
@login_required
def note_index_page():
    """
    用户的笔记
    """
    data = {}
    editor = g.curr_user
    uid = request.args.get('uid', type=int, default=0)

    user = None
    if uid:
        user = User.get(uid)
    if not user:
        user = editor

    form = NoteForm()
    form.uid.data = user.id
    data['form'] = form
    notes, pages = get_user_recent_notes(user, limit=60)
    data['notes'] = notes
    data['pages'] = pages
    return render('/note/index.html', **data)


@note_page.route("/note/index.post", methods=("POST",))
@login_required
def note_index_post_page():
    """
    添加用户笔记
    """
    editor = g.curr_user
    data = {}
    form = NoteForm()
    data['is_error'] = False
    uid = form.uid.data
    user = None
    if uid:
        user = User.get(uid)
    if not user:
        user = editor

    if form.validate():

        note = add_note(form.title.data, form.content.data, user, editor,
                        x=form.x.data, y=form.y.data, z=form.z.data)

        to_redirect = redirect(url_for('note_page.note_index_page', uid=uid))
        return to_redirect
    else:
        data['is_error'] = True

    data['form'] = form
    notes, pages = get_user_recent_notes(user, limit=60)
    data['notes'] = notes
    data['pages'] = pages
    return render('/note/index.html', **data)