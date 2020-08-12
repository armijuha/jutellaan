from app import app
import users
from flask import render_template, redirect, request

@app.route("/")
def index():
    count = users.get_counter()
    return render_template("index.html", count=count)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if users.login(name,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if users.register(name,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti epäonnistui")
