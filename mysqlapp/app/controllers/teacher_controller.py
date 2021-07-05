from mysql.connector.errors import DatabaseError
from app.models.teacher_models import Database
from flask import Flask, json, jsonify, request
from flask_jwt_extended import *
import datetime

mysqldb = Database()

def token(**params):
    dbresult = mysqldb.showTeacherByEmail(**params)
    if dbresult is not None:
        user = {
            "username" : dbresult[1],
            "email" : dbresult[2]
        }
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(user, fresh=True, expires_delta= expires)
        data = {
            "data" : user,
            "token_access": access_token
        }
    else:
        data = {
            "message" : "Email tidak terdaftar"
        }
    return jsonify(data)

def api_get_teachers():
    dbresult = mysqldb.showTeacher()
    result = []
    for items in dbresult:
        user = {
            "id" : items[0],
            "username":items[1],
            "email":items[2],
            "nama":items[3],
            "phone":items[4],
            "guardian_teacher":items[5],
        }
        result.append(user)
    return jsonify(result)

def api_get_teacher(**params):
    dbresult = mysqldb.showTeacherById(**params)
    user = {
            "id" : dbresult[0],
            "username":dbresult[1],
            "email":dbresult[2],
            "nama":dbresult[3],
            "phone":dbresult[4],
            "guardian_teacher":dbresult[5],
    }
    return jsonify(user)

@jwt_required()
def api_post_teacher(**params):
    try:
        mysqldb.insertTeacher(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Teacher succesfully created", "code":"200"})

@jwt_required()
def api_edit_teacher(**params):
    try:
        mysqldb.updateTeacherById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Teacher succesfully edited", "code":"201"})

@jwt_required()
def api_delete_teacher(**params):
    try:
        mysqldb.deleteTeacherById(**params)
    except Exception as e:
        print(e)
    return jsonify({"message": "Teacher succesfully deleted", "code":"201"})