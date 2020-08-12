from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

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
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(name,password):
    hash_value = generate_password_hash(password)
    type = 1
    try:
        sql = "INSERT INTO users (name,password,type) VALUES (:name,:password,:type)"
        db.session.execute(sql, {"name":name,"password":hash_value,"type":type})
        db.session.commit()
    except:
        return False
    return login(name,password)

def user_id():
    return session.get("user_id",0)
