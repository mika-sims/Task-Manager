# Import render_template function for template rendering
from flask import render_template, request

# Import app and db variables from main taskmanager folder
from taskmanager import app, db

# Import models classes from models.py file
from taskmanager.models import Category, Task

# App route 
@app.route("/")
def home():
    return render_template("tasks.html")

# App route for categories.html
@app.route("/categories")
def categories():
    return render_template("categories.html")

# App route for add_category.html
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POst":
        category = Category(category_name=request.form.get("category_name"))
    return render_template("add_category.html")