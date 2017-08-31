#!/usr/bin/env python

from os import getenv
from online import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

env = getenv("ONLINE_ENV", "dev")

application = create_app("%s.cfg" % env)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

