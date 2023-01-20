# Import render_template function for template rendering
from flask import render_template

# Import app and db variables from main taskmanager folder
from taskmanager import app, db

# Import models classes from models.py file
from taskmanager.models import Category, Task

# App route 
@app.route("/")
def home():
    return render_template("tasks.html")