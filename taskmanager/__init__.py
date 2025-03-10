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

# Get database URL from environment variables
uri = os.getenv("DATABASE_URL")

# Ensure the URI exists before using it
if not uri:
    raise ValueError("DATABASE_URL is not set. Please configure it in Render.")

# Replace old Heroku-style database URLs
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)

# Import routes file
from taskmanager import routes
