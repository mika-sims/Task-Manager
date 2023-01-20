# Import db variable from taskmanager folder
from taskmanager import db


class Category(db.Model):
    # Schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete",lazy=True)
    
    def __repr__(self):
    # Represent itself in the form of a string
        return self.category_name