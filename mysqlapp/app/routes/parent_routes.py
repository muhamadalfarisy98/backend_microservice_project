from app import app
from app.controllers import parent_controller
from flask import Blueprint, request

parent_blueprint = Blueprint("parent_routes",__name__)

@app.route('/parents', methods = ['GET'])
def get_parents():
    return parent_controller.api_get_parents()

@app.route('/parent', methods = ['GET'])
def get_parent():
    params = request.json
    return parent_controller.api_get_parent(**params)

@app.route('/parent', methods = ['POST'])
def post_parent():
    params = request.json
    return parent_controller.api_post_parent(**params)

@app.route('/parent', methods = ['PUT'])
def edit_parent():
    params = request.json
    return parent_controller.api_edit_parent(**params)

@app.route('/parent', methods = ['DELETE'])
def delete_parent():
    params = request.json
    return parent_controller.api_delete_parent(**params)

@app.route("/parent/request_token", methods= ["GET"])
def requestToken():
    params = request.json
    return parent_controller.token(**params)