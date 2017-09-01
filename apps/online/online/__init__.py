# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flask_uploads import configure_uploads

from theme import theme
from .db import db
from .views import views
from .utils import photos

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
    configure_uploads(app, (photos,))

    return app
