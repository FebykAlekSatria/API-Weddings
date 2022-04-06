from flask import request
from query import *

def weddings():
    if request.method =='GET':
        try :
            params = request.get_json()
            id_user = params['id_user']
            query = 'SELECT * FROM "weddings" WHERE id_user = %s'
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
            lat = params['lat']
            long = params['long']
            photo = params['photo']
            date = params['date']
            query = 'INSERT INTO "weddings" (id_user, lat, long, photo, date) VALUES (%s,%s, %s, %s, %s, %s)'
            params = (id_user, lat, long, photo, date)
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
            lat = params['lat']
            long = params['long']
            photo = params['photo']
            date = params['date']
            query = 'UPDATE "detail_weddings" SET lat = %s, long = %s,  photo = %s, date = %s WHARE id_user = %s'
            params = (lat, long, photo, date, id_user)
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
            query = 'DELETE FROM "weddings" WHERE id_user = %s'
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