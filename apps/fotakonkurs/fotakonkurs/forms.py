from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_security.forms import LoginForm as DefaultLoginForm
from flask_babelex import lazy_gettext as _
from wtforms.fields import html5

class UploadForm(FlaskForm):
    email = html5.EmailField()
    photo = FileField()

    @property
    def name_from_email(self):
        try:
            return self._name_from_email
        except:
            try:
                name = self.email.data.split('@')[0] 
                self._name_from_email = name
                return name
            except:
                return ''

class LoginForm(DefaultLoginForm):

    def validate(self):
        if super(LoginForm, self).validate():
            return True
        self.email.errors       = []
        self.password.errors    = []
        self.errors['submit'] = _('Invalid email and/or password')
        return False
