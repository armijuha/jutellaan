from app import app
import users
import categories
import threads
import messages
from flask import render_template, redirect, request, url_for, session

@app.route("/")
def index():
    list = categories.get_list()
    count_users = users.get_counter()
    count_messages = messages.get_counter()
    return render_template("index.html", list=list, count_users=count_users, count_messages=count_messages)

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
            return render_template("error.html",message="Väärä tunnus tai salasana, yritä uudestaan")

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
            return render_template("error.html",message="Rekisteröinti epäonnistui, "\
            "kokeile uudestaan toisella nimellä")

@app.route("/<int:id>", methods=["GET", "POST"])
def thread(id):
    if request.method == "GET":
        category_name = categories.get_name(id)
        list = threads.get_list(id)
        return render_template("threads.html", category_name=category_name, list=list)

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        thread_name = request.form["thread_name"]
        if threads.send(thread_name, id):
            return redirect(request.url)
        else:
            return render_template("error.html", message="Keskustelun avaaminen ei onnistunut, "\
            "tarkista oletko kirjautuneena sisään tai onko saman niminen keskustelu jo olemassa.")

@app.route("/<int:category_id>/<int:thread_id>", methods=["GET", "POST"])
def message(category_id, thread_id):
    if request.method == "GET":
        category_name = categories.get_name(category_id)
        thread_name = threads.get_name(thread_id)
        list = messages.get_list(category_id, thread_id)
        return render_template("messages.html", category_name=category_name, thread_name=thread_name,\
        list=list, category_id=category_id, thread_id=thread_id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        content = request.form["content"]
        if messages.send(content, category_id, thread_id):
            return redirect(request.url)
        else:
            return render_template("error.html", message="Viestin lähetys ei onnistunut, "\
            "tarkista oletko kirjautunut sisään.")

@app.route("/<int:category_id>/<int:thread_id>/<int:message_id>", methods=["GET", "POST"])
def edit_message(category_id, thread_id, message_id):
    if request.method == "GET":
        content = messages.get_one(message_id)
        return render_template("edit_message.html", content=content)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        choice = request.form["edit"]
        new_content = request.form["content"]
        if choice == "1":
            if messages.hide(message_id):
                return redirect(url_for('message', category_id=category_id, thread_id=thread_id))
            else:
                return render_template("error.html", message="Vain viestin lähettäjä voi muokata viestiä")
        if choice == "2":
            if messages.edit(message_id, new_content):
                return redirect(url_for('message', category_id=category_id, thread_id=thread_id))
            else:
                return render_template("error.html", message="Vain viestin lähettäjä voi muokata viestiä")
        return redirect(url_for('message', category_id=category_id, thread_id=thread_id))

