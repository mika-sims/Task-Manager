import re

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
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

# Instance of SQLAlchemy() class
db = SQLAlchemy(app)

# Import routes file
from taskmanager import routes