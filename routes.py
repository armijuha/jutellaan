from app import app
import users
from flask import render_template

@app.route("/")
def index():
    count = users.get_counter()
    return render_template("index.html", count=count)

