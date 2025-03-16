from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    TRN = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    MaidenName = db.Column(db.String(80))
    Address = db.Column(db.String(128))
    Email = db.Column(db.String(80))
    DOB = db.Column(db.Date)
    Telephone = db.Column(db.Integer)
    MaritalStatus = db.Column(db.String(80))
    Occupation = db.column(db.String(128))
    Gender = db.Column(db.String(80))
    NIS = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.column(db.String(128))
   
    def __init__(self, Title,first_name, last_name, MaidenName, Address, Email, DOB, Telephone, MaritalStatus, Occupation, Gender, NIS, username, password):
        self.Title = Title
        self.first_name = first_name
        self.last_name = last_name
        self.MaidenName = MaidenName
        self.Address = Address
        self.Email = Email
        self.DOB = DOB
        self.Telephone = Telephone
        self.MaritalStatus = MaritalStatus
        self.Occupation = Occupation
        self.Gender = Gender
        self.NIS = NIS
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        super().__init__()    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)