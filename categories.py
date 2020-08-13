from db import db

def get_list():
    sql = "SELECT name, description, type FROM categories ORDER BY id"
    result = db.session.execute(sql)
    return result.fetchall()
