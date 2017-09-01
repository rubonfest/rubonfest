# -*- coding: utf-8 -*-
from flask import session, abort
from flask_uploads import UploadSet, IMAGES
from functools import wraps

photos = UploadSet('photos', IMAGES)

def authorized_view(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            if session['authorized']:
                return f(*args, **kwargs)
        except KeyError:
            pass
        abort(401)
    return decorator

