from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_security.forms import LoginForm as DefaultLoginForm
from flask_security import current_user
from flask_babelex import gettext as _, lazy_gettext as l_
from wtforms import validators
from wtforms.fields import html5

class UploadForm(FlaskForm):
    email = html5.EmailField(
            validators=(
                validators.Email(message=_('This email address looks like invalid one')),
                validators.Length(min=1, max=50, message=_("Wow, sorry, this email address is too long")),
                validators.DataRequired(message=_('Please, leave us your email address'))
            ),
            description=l_('Your email address to get in touch with you')
    )
    photo = FileField(l_('Photo'),
            validators=(
                FileRequired(message=_("Oops! You probably want to upload a photo here")),
                FileAllowed(['jpg', 'jpeg', 'png'], message=_('Notice, only photos with .jpg (.jpeg) or .png extensions are allowed'))
            ), 
            description=l_('Your photo in .jpg(.jpeg) or .png format')
    )

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        try:
            self.email.data = current_user.email
        except AttributeError:
            pass

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
