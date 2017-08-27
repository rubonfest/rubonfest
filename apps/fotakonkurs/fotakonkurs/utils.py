from os import path
from flask import url_for, current_app

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
