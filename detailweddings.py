from flask import request
from query import *

def detailweddings():
    if request.method =='GET':
        try :
            params = request.get_json()
            id_user = params['id_user']
            query = 'SELECT * FROM "detail_weddings" WHERE id_user = %s'
            data = selectbyid(query, (id_user))
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
            date = params['date']
            location = params['location']
            time = params['time']
            query = 'INSERT INTO "detail_weddings" (id_user, name, date, location, time) VALUES (%s,%s, %s, %s, %s)'
            params = (id_user, name, date, location, time)
            count = insert(query, params)
            return {
                'message' : 'sucsess',
                'data' : count
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
            date = params['date']
            location = params['location']
            time = params['time']
            query = 'UPDATE "detail_weddings" SET name = %s, date = %s, location = %s, time = %s WHARE id_user = %s'
            params = (name, date, location, time, id_user)
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
            query = 'DELETE FROM "detail_weddings" WHERE id_user = %s'
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