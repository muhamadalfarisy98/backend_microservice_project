from mysql.connector.errors import DatabaseError
from app.models.sesi_models import Database
from flask import Flask, json, jsonify, request
from flask_jwt_extended import *
import datetime

mysqldb = Database()

def api_get_sesi():
    dbresult = mysqldb.showSesi()
    result = []
    for items in dbresult:
        user = {
            "jadwal_id" : items[1],
            "subject_id" : items[2],
            "time_start" : str(datetime.datetime.strptime(str(items[3]),'%H:%M:%S').time()),
            "time_end" : str(datetime.datetime.strptime(str(items[4]),'%H:%M:%S').time()),
            "teacher_id" : items[5]
        }
        result.append(user)
    return jsonify(result)

@jwt_required()
def api_post_sesi(**params):
    try:
        mysqldb.insertSesi(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Sesi succesfully created", "code":"200"})

@jwt_required()
def api_edit_sesi(**params):
    try:
        mysqldb.updateSesiById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Sesi succesfully edited", "code":"201"})

@jwt_required()
def api_delete_sesi(**params):
    try:
        mysqldb.deleteSesiById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Sesi succesfully deleted", "code":"201"})