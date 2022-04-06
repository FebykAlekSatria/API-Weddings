from flask import request
from query import *
import random
import string

def visitor():
    if request.method =='GET':
        try :
            params = request.get_json()
            id_user = params['id_user']
            query = 'SELECT * FROM "visitor" WHERE id_user = %s'
            data = selectbyid(query, (id_user,))
            return {
                'message': 'sucsess',
                'data': data
            }
        except:
            return{
                'message': 'error',
            }
    elif request.method == 'POST':
        try:
            params = request.get_json()
            id = str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(13)))
            id_user = params['id_user']
            name = params['name']
            comment = params['comment']
            link = params['link']
            desc = params['desc']
            postgres_insert_query = """ INSERT INTO "visitor" (id_user, name, comment, link, "desc", id) VALUES (%s,%s, %s, %s, %s, %s)"""
            record_to_insert = (id_user,name , comment, link, desc, id)
            count = insert(postgres_insert_query, record_to_insert)
            return {
                'message': 'sucsess',
                'data': count
            }
        except:
            return{
                'message': 'error',
            }
    elif request.method == 'PATCH':
        try:
            params = request.get_json()
            id = params['id']
            name = params['name']
            comment = params['comment']
            link = params['link']
            desc = params['desc']
            postgres_insert_query = """ UPDATE "visitor" SET name = %s, comment = %s, link = %s, "desc" = %s WHERE id = %s"""
            record_to_insert = (name, comment, link, desc, id)
            count = update(postgres_insert_query, record_to_insert)
            return {
                'message': 'sucsess',
                'data': count
            }
        except:
            return{
                'message': 'error',
            }
    elif request.method == 'DELETE':
        try:
            params = request.get_json()
            id = params['id']
            postgres_insert_query = """ DELETE FROM "visitor" WHERE id = %s"""
            record_to_insert = (id,)
            count = delete(postgres_insert_query, record_to_insert)
            return {
                'message': 'sucsess',
                'data': count
            }
        except:
            return{
                'message': 'error',
            }
    
def getdesc():
    try :
        params = request.get_json()
        id_user = params['id_user']
        desc = params['desc']
        query = 'SELECT * FROM "visitor" WHERE id_user = %s and "desc" = %s'
        params = (id_user, desc)
        data = selectbyid(query, params)
        return {
            'message': 'sucsess',
            'data': data
        }
    except:
        return{
            'message': 'error',
        }
