from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField,PasswordField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class UpdateInfoForm(FlaskForm):
    document_type = SelectField(
        'Document to update',
        choices=[
            ('trn', 'TRN'), ('birth_certificate', 'Birth Certificate'),
            ('passport', 'Passport'), ('nis', 'NIS'),
            ('drivers_license', 'Driver\'s License'), ('voters_id', 'Voter\'s ID')
        ],
        validators=[InputRequired()]
    )
    
    title = SelectField(
        'Title',
        choices=[
          ('mr.', 'Mr.'),  ('ms.', 'Ms.'), ('mrs.', 'Mrs.'),
        ],
        validators=[InputRequired()]
    )

    first_name = StringField('First Name', validators=[InputRequired()])
    middle_name = StringField('Middle Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    married_name = StringField('Married Name')
    DOB = StringField('Date of Birth', validators=[InputRequired()])
    
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    trn = StringField('TRN', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
