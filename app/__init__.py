from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
from app import views