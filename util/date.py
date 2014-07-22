# -*- coding: utf-8 -*-
import datetime

__author__ = 'myth'


def add_hours_to_day(day, offset):
    """
    Returns the date n hours before or after day
    """
    return day + datetime.timedelta(hours=offset)


def add_days_to_day(day, offset):
    """
    Returns the date n days before or after day
    """
    return day + datetime.timedelta(days=offset)