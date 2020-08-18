from db import db
import users

def get_list(category_id):
    sql = "SELECT id, name , category_id FROM threads WHERE category_id=:category_id ORDER BY id"
    result = db.session.execute(sql, {"category_id":category_id})
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM threads WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, category_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO threads(name, category_id) VALUES (:name, :category_id)"
    db.session.execute(sql, {"name":name, "category_id":category_id})
    db.session.commit()
    return True

