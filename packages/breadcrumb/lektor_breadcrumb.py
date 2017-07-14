# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from breadcrumb import breadcrumb_for_page

class BreadcrumbPlugin(Plugin):
    name = u'lektor-breadcrumb'
    description = u'Add your description here.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['breadcrumb'] = breadcrumb_for_page
