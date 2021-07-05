from app.models.subject_models import *
from flask import jsonify, request
from flask_jwt_extended import *
import json, datetime

def api_get_subjects():
    res = showSubject()
    return jsonify(res)

def api_get_subject(**params):
    res = showSubjectById(**params)
    return jsonify(res)

@jwt_required()
def api_post_subject(**params):
    insertSubject(**params)
    return jsonify({"message": "Subject succesfully created", "code":"200"})

@jwt_required()
def api_edit_subject(**params):
    res = updateSubjectById(**params)
    return jsonify(res)

@jwt_required()
def api_delete_subject(**params):
    res = deleteSubjectById(**params)
    return jsonify(res)