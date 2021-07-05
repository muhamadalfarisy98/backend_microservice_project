from app import app
from app.controllers import student_controller
from flask import Blueprint, request

student_blueprint = Blueprint("student_routes",__name__)

@app.route('/students', methods = ['GET'])
def get_students():
    return student_controller.api_get_students()

@app.route('/student', methods = ['GET'])
def get_student():
    params = request.json
    return student_controller.api_get_student(**params)

@app.route('/student', methods = ['POST'])
def post_student():
    params = request.json
    return student_controller.api_post_student(**params)

@app.route('/student', methods = ['PUT'])
def edit_student():
    params = request.json
    return student_controller.api_edit_student(**params)

@app.route('/student', methods = ['DELETE'])
def delete_student():
    params = request.json
    return student_controller.api_delete_student(**params)

@app.route("/student/request_token", methods= ["GET"])
def student_requestToken():
    params = request.json
    return student_controller.token(**params)