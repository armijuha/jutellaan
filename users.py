from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def get_counter():
    result = db.session.execute("SELECT COUNT(*) FROM users")
    count = result.fetchone()[0]
    return count

def login(name,password):
    sql = "SELECT password, id FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = name
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]

def register(name,password):
    if len(name) < 3 or len(name) > 20:
        return False
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (name,password,type) VALUES (:name,:password, '1')"
        db.session.execute(sql, {"name":name,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(name,password)

def user_id():
    return session.get("user_id",0)
