# -*- coding: utf-8 -*-
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import fields, validators

from .db import all_categories

_login_invalid_message = u"Хібныя звесткі для ўваходу, паспрабуйце яшчэ"

class LoginValidator(object):
    def __call__(self, form, field):
        try:
            if field.data == current_app.config['ONLINE_LOGIN']:
                return
        except KeyError:
            pass
        raise validators.StopValidation(_login_invalid_message)

class PasswordValidator(object):
    def __call__(self, form, field):
        try:
            if field.data == current_app.config['ONLINE_PASS']:
                return 
        except KeyError:
            pass
        raise validators.StopValidation(_login_invalid_message)

class LoginForm(FlaskForm):
    login = fields.StringField(u"Вашае імя", validators=(
            validators.InputRequired(message=u"Увядзіце, калі ласка, імя"),
            validators.Length(max=50, message=u"Задоўгае імя"),
            LoginValidator()
        )
    )
    password = fields.PasswordField(u"Ваш пароль", validators=(
            validators.InputRequired(message=u"Увядзіце, калі ласка, пароль"),
            validators.Length(max=100, message=u"Задоўгі пароль"),
            PasswordValidator()
        )
    )

class MessageForm(FlaskForm):
    category = fields.SelectField(u"Катэгорыя", 
            validators=(
                validators.InputRequired(message=u"Выберыце, калі ласка, катэгорыю паведамлення"),
            )
    )
    message = fields.TextAreaField(u"Паведамленне",
            validators=(
                validators.InputRequired(message=u"Як жа без паведамлення?"),
                validators.Length(max=500, message=u"Калі ласка, не больш за 500 сімвалаў")
            )
    )

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.category.choices=[ (name, name) for name in all_categories]
        self.category.choices.insert(0, ("", u"-- катэгорыя --"))

