import os
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 10000)),
        debug=os.environ.get("DEBUG", "False") == "True"
    )
