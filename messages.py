
from db import db
import users

def get_counter():
    result = db.session.execute("SELECT COUNT (*) FROM messages")
    return result.fetchone()[0]

def get_list(category_id, thread_id):
    sql = "SELECT M.content, U.name, M.time, M.id FROM messages M, users U "\
    "WHERE category_id=:category_id AND thread_id=:thread_id AND user_id=U.id "\
    "AND M.visibility=True ORDER BY M.id"
    result = db.session.execute(sql, {"category_id":category_id, "thread_id":thread_id})
    return result.fetchall()

def send(content, category_id, thread_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages(content, category_id, thread_id, user_id, time, visibility) "\
    "VALUES (:content, :category_id, :thread_id, :user_id, NOW(), True)"
    db.session.execute(sql, {"content":content, "category_id":category_id, "thread_id":thread_id, "user_id":user_id})
    db.session.commit()
    return True

def get_one(id):
    sql = "SELECT content FROM messages WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def hide(id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "SELECT user_id FROM messages WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    message_user_id = result.fetchone()[0]
    if user_id == message_user_id:
        sql = "UPDATE messages SET visibility=False WHERE id=:id"
        result = db.session.execute(sql, {"id":id})
        db.session.commit()
        return True
    return False

def edit(id, content):
    user_id = users.user_id()
    sql = "SELECT user_id FROM messages WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    message_user_id = result.fetchone()[0]
    if user_id == message_user_id:
        sql = "UPDATE messages SET content=:content WHERE id=:id" 
        result = db.session.execute(sql, {"id":id, "content":content})
        db.session.commit()
        return True
    return False
