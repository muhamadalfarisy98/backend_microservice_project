from app import app
from app.controllers import class_controller
from flask import Blueprint, request

class_blueprint = Blueprint("class_routes",__name__)

@app.route('/class', methods = ['GET'])
def get_class():
    return class_controller.api_get_classes()

@app.route('/class/students', methods = ['GET'])
def get_student_class():
    params = request.json
    return class_controller.api_get_students_class(**params)

@app.route('/class', methods = ['POST'])
def post_class():
    params = request.json
    return class_controller.api_post_class(**params)

@app.route('/class', methods = ['PUT'])
def edit_class():
    params = request.json
    return class_controller.api_edit_class(**params)

@app.route('/class', methods = ['DELETE'])
def delete_class():
    params = request.json
    return class_controller.api_delete_class(**params)
