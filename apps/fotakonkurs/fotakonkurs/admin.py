from os import path
from flask import redirect, abort, request, url_for, current_app
from flask_security import SQLAlchemyUserDatastore, current_user, Security
from flask_admin import form, Admin, helpers
from flask_admin.contrib import sqla
from flask_babelex import lazy_gettext as _
from jinja2 import Markup
from .db import db, User, Role, UserFile
from .forms import LoginForm
from .utils import user_file_preset_url

class ClosedView(object):
    
    def is_accessible(self):
        if current_app.config.get('FOTAKONKURS_ADMIN_OPEN', False):
            return True
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if self._check_role():
            return True
        return False

    def _check_role(self):
        return current_user.has_role('superuser')

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))

class ClosedModelView(ClosedView, sqla.ModelView):
    pass

class ManagerView(ClosedView, sqla.ModelView):

    def _check_role(self):
        return (super(ManagerView, self)._check_role() 
                or current_user.has_role('manager'))

class UserAdmin(ClosedModelView):
    pass

class RoleAdmin(ClosedModelView):
    pass

class UserFileAdmin(ManagerView):

    can_create = False

    def _list_thumbnail(view, context, model, name):
        if not model.filename:
            return''
        big_image_url = user_file_preset_url(model, 'big')
        sml_image_url = user_file_preset_url(model, 'sml')
        return Markup('<a href="%s" target="_blank"><img src="%s" /></a>' % (
            big_image_url,
            sml_image_url
        ))

    column_formatters = {
            'filename': _list_thumbnail,
    }

views = (
        UserAdmin(User, db.session, name=_('User')),
        RoleAdmin(Role, db.session, name=_('Role')),
        UserFileAdmin(UserFile, db.session, name=_('User File'))
)
admin = Admin(template_mode='bootstrap3')
admin.add_views(*views)

def init_app(app):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, login_form=LoginForm, datastore=user_datastore)
    admin.init_app(app)

    @security.context_processor
    def security_context_processor():
        return dict(
                admin_base_template=admin.base_template,
                admin_view=admin.index_view,
                h=helpers,
                get_url=url_for
        )


