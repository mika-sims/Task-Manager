# Import OS module
import os

# Import app variable from taskmanager folder
from taskmanager import app

# Run application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )