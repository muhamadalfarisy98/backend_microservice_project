from app.models.parent_models import *
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

def token(**params):
    res = showParentByEmail(**params)
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

def api_get_parents():
    res = showParent()
    return jsonify(res)

def api_get_parent(**params):
    res = showParentById(**params)
    return jsonify(res)

@jwt_required()
def api_post_parent(**params):
    insertParent(**params)
    return jsonify({"message": "Parent succesfully created", "code":"200"})

@jwt_required()
def api_edit_parent(**params):
    res = updateParentById(**params)
    return jsonify(res)

@jwt_required()
def api_delete_parent(**params):
    res = deleteParentById(**params)
    return jsonify(res)