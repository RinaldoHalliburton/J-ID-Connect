from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
#mysql = SQLAlchemy(app)

# Import views (routes) after initializing app and extensions
from app import views
