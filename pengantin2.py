from flask import request
from query import *

def pengantin2():
    if request.method =='GET':
        try :
            params = request.get_json()
            id_user = [str(params['id_user'])]
            query = 'SELECT * FROM "pengantin_2" WHERE id_user = %s'
            data = selectbyid(query, id_user)
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
            id_user = params['id_user']
            name = params['name']
            child_to = params['child_to']
            mother = params['mother']
            father = params['father']
            photo = params['photo']
            gender = params['gender']
            query = 'INSERT INTO "pengantin_2" (id_user, name, child_to, mother, father, photo, gender) VALUES (%s,%s, %s, %s, %s, %s, %s)'
            params = (id_user, name, child_to, mother, father, photo, gender)
            count = insert(query, params)
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
            id_user = params['id_user']
            name = params['name']
            child_to = params['child_to']
            mother = params['mother']
            father = params['father']
            photo = params['photo']
            gender = params['gender']
            query = 'UPDATE "pengantin_2" SET name = %s, child_to = %s, mother= %s, father = %s, photo = %s, gender = %s WHARE id_user = %s'
            params = (name, child_to, mother, father, photo, gender, id_user)
            count = update(query, params)
            return {
                'message' : 'sucsess',
                'data' : count
            }
        except:
            return{
                'message': 'error',
            }
    elif request.method == 'DELETE':
        try:
            params = request.get_json()
            id_user = params['id_user']
            query = 'DELETE FROM "pengantin_2" WHERE id_user = %s'
            params = (id_user,)
            count = delete(query, params)
            return {
                'message' : 'sucsess',
                'data' : count
            }
        except:
            return{
                'message': 'error',
            }