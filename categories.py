from db import db

def get_list():
    sql = "SELECT id, name, description, type FROM categories ORDER BY id"
    result = db.session.execute(sql)
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM categories WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]
