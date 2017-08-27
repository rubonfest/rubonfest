import os
from json import dumps
from flask          import (Blueprint, render_template, request, 
                            redirect, flash, current_app, url_for,
                            abort
                            )
from werkzeug.utils import secure_filename
from flask_babelex  import gettext as _
from PIL import Image

from .forms import UploadForm
from .db    import UserFile, db
from .utils import user_file_dict

views = Blueprint('views', __name__)

@views.route('/upload', methods=[ 'GET' ])
def get_upload():
    form = UploadForm()
    return render_template('upload.html', form=form)

@views.route('/upload', methods=[ 'POST' ])
def post_upload():
    form = UploadForm()
    if form.is_submitted():
        f = request.files['photo']
        filename    = secure_filename(f.filename)
        # place to refactor
        public_path = os.path.join(os.path.dirname(__file__), current_app.static_folder, 'uploads', form.name_from_email)
        user_upload_path = os.path.join(current_app.config['FOTAKONKURS_UPLOADS_PATH'], form.name_from_email)
        big_preset_path  = os.path.join(public_path, 'big')
        mid_preset_path  = os.path.join(public_path, 'mid')
        sml_preset_path  = os.path.join(public_path, 'sml')
        try:
            os.mkdir(user_upload_path)
        except OSError:
            pass
        try:
            os.mkdir(public_path)
        except OSError:
            pass
        try:
            os.mkdir(big_preset_path)
        except OSError:
            pass
        try:
            os.mkdir(mid_preset_path)
        except OSError:
            pass
        try:
            os.mkdir(sml_preset_path)
        except OSError:
            pass
        saved_filepath = os.path.join(user_upload_path, filename)
        try:
            f.save(saved_filepath)
            orig   = Image.open(saved_filepath)
            big    = orig.copy()
            width, height = orig.size
            side   = min(width, height)
            left   = (width - side) / 2
            top    = (height - side) / 2
            right  = left + side
            bottom = top + side
            mid  = orig.crop((left, top, right, bottom))
            sml  = mid.copy()
            mid.thumbnail((300, 300))
            sml.thumbnail((100, 100))
            big.save(os.path.join(big_preset_path, filename))
            mid.save(os.path.join(mid_preset_path, filename))
            sml.save(os.path.join(sml_preset_path, filename))
        except IOError:
            flash(_('The error ocurred while saving file'))
            return render_template('upload.html', form=UploadForm()) 
        file_model = UserFile(f.filename, filename, form.name_from_email) 
        db.session.add(file_model)
        db.session.commit()
        flash(_('Thank you, the file was successfully uploaded'))
        return redirect(url_for('.get_upload'))
    flash(_("Oops! You've got an error"))
    return render_template('upload.html', form=form)

@views.route('/jsonp/<string:endpoint>', methods=[ 'GET' ])
def jsonp(endpoint):
    user_files = UserFile.query.all()
    return 'try { fotakonkurs.%s(%s); } catch (e) { console.log(e.message); }' % (
            endpoint, dumps({'records': map(user_file_dict, user_files)})
    )
