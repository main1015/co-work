# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import desc, func
from db.database import db_session
from db.model.note import Note
from db.service.db_util import inquiry_process
from util.date import add_days_to_day

__author__ = 'myth'


def add_note(title, content, user, editor, x=0, y=0, z=0):
    """
    添加笔记
    """

    note = Note()

    note.editor_id = editor.id
    note.editor_nickname = editor.nickname or editor.email

    note.user_id = user.id
    note.nickname = user.nickname or user.email

    note.title = title
    note.content = content
    note.x = x
    note.y = y
    note.z = z

    db_session.add(note)
    db_session.commit()
    return note


def get_user_recent_notes(user, limit=20, page=1):
    """
    获取近期的笔记
    """
    #近期的时间设置未两个月
    now = datetime.datetime.now()
    _date = add_days_to_day(now, -60)
    criterion = [
        Note.user_id == user.id,
        Note.created_at >= _date
    ]
    note_query = Note.query.filter(*criterion)
    note_query = note_query.order_by(desc(Note.created_at))

    count_query = db_session.query(func.count(Note.id))
    count_query = count_query.filter(*criterion)

    notes, pages = inquiry_process(count_query, note_query, limit=limit, page=page)
    return notes, pages
