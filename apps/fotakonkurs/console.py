#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from os import getenv
from flask_migrate import MigrateCommand
from flask_script import Manager
from fotakonkurs import create_app

env = getenv('FOTAKONKURS_ENV', 'dev')
app = create_app('%s.cfg' % env)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
