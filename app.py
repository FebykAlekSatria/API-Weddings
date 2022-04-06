from operator import imod
from flask import Flask, request
from detailweddings import detailweddings
from login import login
from pengantin1 import pengantin1
from pengantin2 import pengantin2
from query import *
from user import user
from visitor import visitor, getdesc
from weddings import weddings

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def apiUser():
    data = user()
    return data

@app.route('/login', methods=['GET'])
def apiLogin():
    data = login()
    return data

@app.route('/visitor', methods=['GET', 'POST','PATCH', 'DELETE'])
def apiVisitor():
    data = visitor()
    return data

@app.route('/visitorgetdesc', methods=['GET'])
def apiDesc():
    data = getdesc()
    return data

@app.route('/pengantin1', methods=['GET', 'POST','PATCH', 'DELETE'])
def apiPengan1():
    data = pengantin1()
    return data

@app.route('/pengantin2', methods=['GET', 'POST','PATCH', 'DELETE'])
def apiPengantin2():
    data = pengantin2()
    return data

@app.route('/detailweddings', methods=['GET', 'POST','PATCH', 'DELETE']) 
def apiDetailWeddings():
    data = detailweddings()
    return data

@app.route('/weddings', methods=['GET', 'POST','PATCH', 'DELETE']) 
def apiWeddings():
    data = weddings()
    return data


if __name__ == '__main__':
     app.run()