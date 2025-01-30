from flask import Flask
from config import Config

app = Flask(__name__)

from app import routes, models, forms
app.config.from_object(Config)