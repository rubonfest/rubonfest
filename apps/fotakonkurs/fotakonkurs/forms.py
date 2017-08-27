from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_security.forms import LoginForm as DefaultLoginForm
from flask_babelex import gettext as _
from wtforms import validators
from wtforms.fields import html5

class UploadForm(FlaskForm):
    email = html5.EmailField(
            validators=(
                validators.Email(message=_('This email address looks like invalid one')),
                validators.Length(50, message=_("Wow, sorry, this email address is too long")),
                validators.DataRequired(message=_('Please, leave us your email address'))
            ),
            description=_('Your email address to get in touch with you')
    )
    photo = FileField(_('Photo'),
            validators=(
                FileRequired(message=_("Oops! You probably want to upload a photo here")),
                FileAllowed(['jpg', 'jpeg', 'png'], message=_('Notice, only photos with .jpg (.jpeg) or .png extensions are allowed'))
            ), 
            description=_('Your photo in .jpg(.jpeg) or .png format')
    )

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
