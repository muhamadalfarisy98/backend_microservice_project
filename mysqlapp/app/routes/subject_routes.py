from app import app
from app.controllers import subject_controller
from flask import Blueprint, request

subject_blueprint = Blueprint("subject_routes",__name__)

@app.route('/subjects', methods = ['GET'])
def get_stubjects():
    return subject_controller.api_get_subjects()

@app.route('/subject', methods = ['GET'])
def get_stubject():
    params = request.json
    return subject_controller.api_get_subject(**params)

@app.route('/subject', methods = ['POST'])
def post_subject():
    params = request.json
    return subject_controller.api_post_subject(**params)

@app.route('/subject', methods = ['PUT'])
def edit_subject():
    params = request.json
    return subject_controller.api_edit_subject(**params)

@app.route('/subject', methods = ['DELETE'])
def delete_subject():
    params = request.json
    return subject_controller.api_delete_subject(**params)