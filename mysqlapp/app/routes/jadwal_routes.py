from app import app
from app.controllers import jadwal_controller
from flask import Blueprint, request

jadwal_blueprint = Blueprint("jadwal_routes",__name__)

@app.route('/jadwal', methods = ['GET'])
def get_jadwal():
    return jadwal_controller.api_get_jadwal()

@app.route('/jadwal/sesi', methods = ['GET'])
def get_sesi_jadwal():
    params = request.json
    return jadwal_controller.api_get_sesi_jadwal(**params)

@app.route('/jadwal', methods = ['POST'])
def post_jadwal():
    params = request.json
    return jadwal_controller.api_post_jadwal(**params)

@app.route('/jadwal', methods = ['PUT'])
def edit_jadwal():
    params = request.json
    return jadwal_controller.api_edit_jadwal(**params)

@app.route('/jadwal', methods = ['DELETE'])
def delete_jadwal():
    params = request.json
    return jadwal_controller.api_delete_jadwal(**params)
