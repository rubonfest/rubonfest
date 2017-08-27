import os
from sqlalchemy.event import listens_for
from .db import UserFile
from .utils import user_file_orig_path, user_file_preset_path

@listens_for(UserFile, 'after_delete')
def handle_delete_user_file(mapper, connection, target):
    orig_path = user_file_orig_path(target)
    big_path  = user_file_preset_path(target, 'big')
    mid_path  = user_file_preset_path(target, 'mid')
    sml_path  = user_file_preset_path(target, 'sml')
    try:
        os.remove(orig_path)
    except OSError:
        pass
    try:
        os.remove(big_path)
    except OSError:
        pass
    try:
        os.remove(mid_path)
    except OSError:
        pass
    try:
        os.remove(sml_path)
    except OSError:
        pass

