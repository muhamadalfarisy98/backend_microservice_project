from mysql.connector.errors import DatabaseError
from app.models.class_models import Database
from flask import Flask, json, jsonify, request
from flask_jwt_extended import *
import datetime

mysqldb = Database()

def api_get_classes():
    dbresult = mysqldb.showClass()
    result = []
    for items in dbresult:
        user = {
            "class_id" : items[0],
            "namakelas":items[1],
            "educational_id":items[2],
            "teacher_id":items[3],
            "seats":items[4]
        }
        result.append(user)
    return jsonify(result)

def api_get_students_class(**params):
    dbresult = mysqldb.showStudentClassById(**params)
    result = []
    for student in dbresult:
        user = {
                "siswa_id" : student[0],
                "namadepan":student[3],
                "namabelakang":student[4],
                "parent_id":student[5],
                "class_id":student[6]
        }
        result.append(user)
    return jsonify(result)

@jwt_required()
def api_post_class(**params):
    try:
        mysqldb.insertClass(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Class succesfully created", "code":"200"})

@jwt_required()
def api_edit_class(**params):
    try:
        mysqldb.updateClassById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Class succesfully edited", "code":"201"})

@jwt_required()
def api_delete_class(**params):
    try:
        mysqldb.deleteClassById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Class succesfully deleted", "code":"201"})