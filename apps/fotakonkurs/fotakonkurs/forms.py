from flask_wtf import FlaskForm
from flask_wtf.file import FileField
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
