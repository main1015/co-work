# -*- coding: utf-8 -*-
from .company.views import company_page
from .note.views import note_page
from .user.views import user_page
from .tool.views import tool_page


__author__ = 'myth'
"""
Created by myth on 15-12-25.
"""


__all__ = [
    "company_page",
    "note_page",
    "user_page",
    "tool_page",
]

pages = __all__
