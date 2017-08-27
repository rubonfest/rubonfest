import string
import random
from os import path
from flask import url_for, current_app
from flask_security.utils import encrypt_password
from .db import User

def user_file_dict(f):
    return {
            'name': f.orig_name,
            'big'   : user_file_preset_url(f, 'big'),
            'mid'   : user_file_preset_url(f, 'mid'),
            'sml'   : user_file_preset_url(f, 'sml')
    }

def user_file_orig_path(f):
    user_upload_path = path.join(current_app.config['FOTAKONKURS_UPLOADS_PATH'], f.filedir)
    return path.join(user_upload_path, f.filename)

def user_file_preset_path(f, preset_name):
    public_path = path.join(path.dirname(__file__), current_app.static_folder, 'uploads', f.filedir)
    return path.join(public_path, preset_name, f.filename)

def user_file_preset_url(f, preset_name):
    return url_for('static', filename='uploads/%s/%s/%s' % (
        f.filedir, preset_name, f.filename))

def create_participant(email):
    u = User()
    u.email = email
    u.password = unicode(encrypt_password(_random_password()))
    return u

def _random_password(length=32):
    SIMPLE_CHARS = string.ascii_letters + string.digits
    return ''.join(random.choice(SIMPLE_CHARS) for i in xrange(length))

