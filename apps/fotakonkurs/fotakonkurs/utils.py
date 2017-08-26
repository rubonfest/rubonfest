from os import path
from flask import url_for

def user_file_dict(f):
    return {
            'name': f.orig_name,
            'big'   : url_for('static', filename='uploads/%s/big/%s' % (f.filedir, f.filename)),
            'mid'   : url_for('static', filename='uploads/%s/mid/%s' % (f.filedir, f.filename)),
            'sml'   : url_for('static', filename='uploads/%s/sml/%s' % (f.filedir, f.filename)),
    }
