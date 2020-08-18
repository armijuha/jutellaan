
from db import db
import users

def get_list(category_id, thread_id):
    sql = "SELECT M.content, U.name, M.time FROM messages M, users U WHERE category_id=:category_id AND thread_id=:thread_id AND user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql, {"category_id":category_id, "thread_id":thread_id})
    return result.fetchall()

def send(content, category_id, thread_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages(content, category_id, thread_id, user_id, time, visibility) VALUES (:content, :category_id, :thread_id, :user_id, NOW(), True)"
    db.session.execute(sql, {"content":content, "category_id":category_id, "thread_id":thread_id, "user_id":user_id})
    db.session.commit()
    return True
