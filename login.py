from flask import request
from query import selectbyid

def login():
    if request.method =='GET':
        try :
            params = request.get_json()
            name = params['name']
            password = params['password']
            query = 'SELECT * FROM "user" WHERE name = %s and password = %s'
            params = (name, password)
            data = selectbyid(query, params)
            return {
                'message': 'Success',
                'data': data
        }
        except:
            return{
                'message': 'error',
            }