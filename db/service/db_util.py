# -*- coding: utf-8 -*-
from math import ceil

__author__ = 'myth'


def inquiry_process(count_query, object_query, limit=10, page=1):
    """
    返回查询结果和分页
    :param count_query:
    :param object_query:
    :param limit:
    :param page:
    :return:
    """

    count = count_query.first()
    if count:
        count = count[0]
    else:
        count = 0
    offset = (page-1)*limit

    pages = Pagination(page, limit, count)
    objects = object_query[offset:page*limit]

    return objects, pages


class Pagination(object):
    """
    Common web page pagination.
    """

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

        self._pages = self.pages

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
                    (self.page - left_current - 1 < num < self.page + right_current) or \
                            num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    def __iter__(self):
        # return iter(self.iter_pages())
        self._pages = list()
        for _page in self.iter_pages():
            if _page:
                self._pages.append(_page)
            else:
                self._pages.append("...")
        return self

    def next(self):
        if not self._pages:
            raise StopIteration
        else:
            return self._pages.pop(0)