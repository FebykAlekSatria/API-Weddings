from query import *
from flask import request
import random
import string

def user():
    if request.method =='GET':
        try :
            query = 'SELECT * FROM "user"'
            data = select(query)
            return {
                'message': 'Success',
                'data': data
            }
        except:
            return{
                'message': 'error',
            }
        
    elif request.method == 'POST':
        try:
            params = request.get_json()
            name = params['name']
            password = params['password']
            id = str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(13)))
            postgres_insert_query = """ INSERT INTO "user" (id, name, password) VALUES (%s,%s, %s)"""
            record_to_insert = (id, name , password)
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
            password = params['password']
            postgres_insert_query = """ UPDATE "user" SET name = %s, password = %s WHERE id = %s"""
            record_to_insert = (name, password, id)
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
            postgres_insert_query = """ DELETE FROM "user" WHERE id = %s"""
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