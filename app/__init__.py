from flask import Flask
from flask_mysqldb import MySQL
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)

# Import views (routes) after initializing app and extensions
from app import views
