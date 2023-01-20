# Import OS module
import os

# Import Flask framework
from flask import Flask

# Import Flask-SQLAlchemy extension
from flask_sqlalchemy import SQLAlchemy

# Import environment variables
if os.path.exists("env.py"):
    import env

# Instance of Flask() class
app = Flask(__name__)

# Environment variables for app configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Instance of SQLAlchemy() class
db = SQLAlchemy(app)