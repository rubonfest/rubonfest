# -*- coding: utf-8 -*-
from flask import Blueprint

theme = Blueprint('theme', __name__, template_folder='templates', 
                                     static_folder='static',
                                     url_prefix='/theme')
