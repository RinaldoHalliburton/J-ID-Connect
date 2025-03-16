from flask import Flask
from flask_mysqldb import MySQL
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'group86'
app.config['MYSQL_PASSWORD'] = 'Intelli@2025'
app.config['MYSQL_DB'] = 'JID'


# Initialize MySQL
mysql = MySQL(app)

# Import views (routes) after initializing app and extensions
from app import views
