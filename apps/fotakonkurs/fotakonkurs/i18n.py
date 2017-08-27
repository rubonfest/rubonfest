# -*- coding: utf-8 -*-
from flask import request, g, abort, current_app, session
from werkzeug.local import LocalProxy

known_locales = {
        'en': dict(title=u'English'),
        'be': dict(title=u'Беларуская'),
        'ru': dict(title=u'Русский')
}
all_locales = known_locales.keys()
default_locale = 'be'


def get_locale():
    url_lang = g.get('lang_code', None)
    if not url_lang is None:
        return url_lang
    if request.args.has_key('lang'):
        session['lang'] = request.args.get('lang')
    if session.has_key('lang'):
        return session.get('lang')
    return default_locale


current_locale = LocalProxy(get_locale)

