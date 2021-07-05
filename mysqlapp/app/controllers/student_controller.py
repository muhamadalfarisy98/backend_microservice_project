from app.models.student_models import *
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

def token(**params):
    res = showStudentByEmail(**params)
    if res :
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(res, fresh=True, expires_delta= expires)
        data = {
            "data" : res,
            "token_access": access_token
        }
    else:
        data = {
            "message" : "Email tidak terdaftar"
        }
    return jsonify(data)

def api_get_students():
    res = showStudent()
    return jsonify(res)

def api_get_student(**params):
    res = showStudentById(**params)
    return jsonify(res)

@jwt_required()
def api_post_student(**params):
    insertStudent(**params)
    return jsonify({"message": "Student succesfully created", "code":"200"})

@jwt_required()
def api_edit_student(**params):
    res = updateStudentById(**params)
    return jsonify(res)

@jwt_required()
def api_delete_student(**params):
    res = deleteStudentById(**params)
    return jsonify(res)