# Import OS module
import os

# Import Flask framework
from flask import Flask

# Import Flask-SQLAlchemy extension
from flask_sqlalchemy import SQLAlchemy

# Import environment variables
if os.path.exists("env.py"):
    import env