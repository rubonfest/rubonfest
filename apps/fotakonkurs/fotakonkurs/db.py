from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserFile(db.Model):
    __tablename__ = "user_file"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filedir     = db.Column(db.Unicode(100))
    filename    = db.Column(db.Unicode(100))
    orig_name   = db.Column(db.Unicode(100))

    def __init__(self, orig_name, filename, filedir):
        self.orig_name = orig_name
        self.filename  = filename
        self.filedir   = filedir

    def __unicode__(self):
        return self.orig_name
