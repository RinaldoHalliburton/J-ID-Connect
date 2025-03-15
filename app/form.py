from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email, InputRequired





class UpdateInfoForm(FlaskForm):
    document_type = SelectField(
        'Document Type',
        choices=[
            ('trn', 'TRN'), ('birth_certificate', 'Birth Certificate'),
            ('passport', 'Passport'), ('nis', 'NIS'),
            ('drivers_license', 'Driver\'s License'), ('voters_id', 'Voter\'s ID')
        ],
        validators=[InputRequired()]
    )

    first_name = StringField('First Name', validators=[InputRequired()])
    middle_name = StringField('Middle Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    married_name = StringField('Married Name')
    DOB = StringField('Date of Birth', validators=[InputRequired()])
    document_file = FileField('Upload Document', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'png', 'jpg', 'jpeg'], 'Only PDF, PNG, JPG, and JPEG files are allowed!')
    ])
    submit = SubmitField('Submit')
