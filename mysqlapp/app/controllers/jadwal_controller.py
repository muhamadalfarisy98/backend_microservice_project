from mysql.connector.errors import DatabaseError
from app.models.jadwal_models import Database
from flask import Flask, json, jsonify, request
from flask_jwt_extended import *
import datetime

mysqldb = Database()

def api_get_jadwal():
    dbresult = mysqldb.showJadwal()
    result = []
    for items in dbresult:
        user = {
            "jadwal_id" : items[0],
            "hari":items[1],
            "class_id":items[2]
        }
        result.append(user)
    return jsonify(result)

def api_get_sesi_jadwal(**params):
    dbresult = mysqldb.showSesiJadwalById(**params)
    result = []
    for items in dbresult:
        user = {
            "sesi_id" : items[0],
            "subject_id" : items[2],
            "time_start" : str(datetime.datetime.strptime(str(items[3]),'%H:%M:%S').time()),
            "time_end" : str(datetime.datetime.strptime(str(items[4]),'%H:%M:%S').time()),
            "teacher_id" : items[5]
        }
        result.append(user)
    return jsonify(result)

@jwt_required()
def api_post_jadwal(**params):
    try:
        mysqldb.insertJadwal(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Class succesfully created", "code":"200"})

@jwt_required()
def api_edit_jadwal(**params):
    try:
        mysqldb.updateJadwalById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Jadwal succesfully edited", "code":"201"})

@jwt_required()
def api_delete_jadwal(**params):
    try:
        mysqldb.deleteJadwalById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Jadwal succesfully deleted", "code":"201"})