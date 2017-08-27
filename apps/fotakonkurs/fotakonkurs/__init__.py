from flask import Flask
from flask_babelex import Babel
from flask_migrate import Migrate
from .views import views
from .db import db
from .i18n import get_locale, default_locale
import admin


def create_app(conf_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update({
        'DEBUG': False,
        'TESTING': False,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    app.config.from_pyfile(conf_filename, silent=True)

    babel = Babel(app)
    babel.localeselector(get_locale)
    db.init_app(app)
    admin.init_app(app)
    Migrate(app, db)
    app.register_blueprint(views, url_defaults={'lang_code': default_locale})
    app.register_blueprint(views, url_prefix='/<lang_code>')
    import db_events
    return app
