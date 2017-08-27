from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin

db = SQLAlchemy()

class UserFile(db.Model):
    __tablename__ = "user_file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filedir     = db.Column(db.Unicode(100))
    filename    = db.Column(db.Unicode(100))
    orig_name   = db.Column(db.Unicode(100))
    user_id     = db.Column(db.ForeignKey('users.id'))
    user        = db.relationship('User', backref="files")

    def __init__(self, orig_name, filename, filedir, user):
        self.orig_name = orig_name
        self.filename  = filename
        self.filedir   = filedir
        self.user      = user

    def __unicode__(self):
        return self.orig_name

users_roles = db.Table(
        'users_roles',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name  = db.Column(db.String(100), unique=True, nullable=False)

    def __unicode__(self):
        return unicode(self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Unicode(300), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    roles = db.relationship(Role, secondary='users_roles', 
            backref=db.backref('users', lazy='dynamic'))

    def __unicode__(self):
        return unicode(self.email)
