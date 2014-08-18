# -*- coding: utf-8 -*-
from functools import partial
from setting.domain import S_DOMAIN
from worker.lib.context import Context

__author__ = 'myth'


def register_global(jinja2_env):

    context = Context()

    css = partial(context.css, domain=S_DOMAIN)
    script = partial(context.js, domain=S_DOMAIN)

    jinja2_env.globals['css'] = css
    jinja2_env.globals['script'] = script
