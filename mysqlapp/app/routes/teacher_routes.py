from app import app
from app.controllers import teacher_controller
from flask import Blueprint, request

teacher_blueprint = Blueprint("teacher_routes",__name__)

@app.route('/teachers', methods = ['GET'])
def get_teachers():
    return teacher_controller.api_get_teachers()

@app.route('/teacher', methods = ['GET'])
def get_teacher():
    params = request.json
    return teacher_controller.api_get_teacher(**params)

@app.route('/teacher', methods = ['POST'])
def post_teacher():
    params = request.json
    return teacher_controller.api_post_teacher(**params)

@app.route('/teacher', methods = ['PUT'])
def edit_teacher():
    params = request.json
    return teacher_controller.api_edit_teacher(**params)

@app.route('/teacher', methods = ['DELETE'])
def delete_teacher():
    params = request.json
    return teacher_controller.api_delete_teacher(**params)

@app.route("/teacher/request_token", methods= ["GET"])
def get_teacher_token():
    params = request.json
    return teacher_controller.token(**params)