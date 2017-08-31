# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate

from theme import theme
from .db import db
from .views import views

def create_app(configfile):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update({
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "DEBUG": False,
        "TESTING": False
    })
    app.config.from_pyfile(configfile, silent=True)
    db.init_app(app)
    app.register_blueprint(views)
    app.register_blueprint(theme)
    Migrate(app, db)

    return app
