from flask import session
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_security.forms import LoginForm as DefaultLoginForm
from flask_security import current_user
from flask_babelex import gettext as _, lazy_gettext as l_
from wtforms import validators
from wtforms.fields import html5, IntegerField, Label
from random import randint, choice

class CaptchaField(IntegerField):

    def __init__(self, session_key, *args, **kwargs):
        self.session_key = session_key
        if not kwargs['_form'].is_submitted():
            label = self._generate()
        else:
            label = ''
        super(CaptchaField, self).__init__(label, *args, **kwargs)

    def _generate(self):
        op = choice(('-', '+'))
        num1 = randint(0, 10)
        num2 = randint(0,10)
        check_result = num1 + num2 if op == '+' else num1 - num2
        session[self.session_key] = check_result
        return "%d %s %d = " % (num1, op, num2)

    def regenerate(self):
        label = self._generate()
        self.label = Label(self.id, label)


class CaptchaValidator(object):

    def __init__(self, message=None):
        self.message = message
    
    def __call__(self, form, field):
        if not session.has_key(field.session_key) or not field.data == session[field.session_key]:
            raise validators.StopValidation(self.message)

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
    captcha = CaptchaField('upload_check', validators=(
            validators.DataRequired(message=_('Please, solve the equation')),
            CaptchaValidator(_('Equation check failed. Please, try again'))
        ),
        description=l_('What is the equation result?')
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
