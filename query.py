from config import *

def select(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def selectbyid(query, id_user):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query,id_user)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def insert(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    count = cur.rowcount
    cur.close()
    conn.close()
    return count

def delete(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    count = cur.rowcount
    cur.close()
    conn.close()
    return count

def update(query, id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, id)
    conn.commit()
    count = cur.rowcount
    cur.close()
    conn.close()
    return count