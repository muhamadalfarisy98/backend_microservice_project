from app import app
from app.controllers import sesi_controller
from flask import Blueprint, request

sesi_blueprint = Blueprint("sesi_routes",__name__)

@app.route('/sesi', methods = ['GET'])
def get_sesi():
    return sesi_controller.api_get_sesi()

@app.route('/sesi', methods = ['POST'])
def post_sesi():
    params = request.json
    return sesi_controller.api_post_sesi(**params)

@app.route('/sesi', methods = ['PUT'])
def edit_sesi():
    params = request.json
    return sesi_controller.api_edit_sesi(**params)

@app.route('/sesi', methods = ['DELETE'])
def delete_sesi():
    params = request.json
    return sesi_controller.api_delete_sesi(**params)
