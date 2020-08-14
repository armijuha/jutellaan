from db import db

def get_list(category_id):
    sql = "SELECT id, name FROM threads WHERE category_id=:category_id ORDER BY id"
    result = db.session.execute(sql, {"category_id":category_id})
    return result.fetchall()
