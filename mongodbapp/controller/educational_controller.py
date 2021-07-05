from pymongo import MongoClient
from models.educational_models import database as db
import csv,json
from bson.objectid import ObjectId
import logging
_logger = logging.getLogger(__name__)


db = db()

def objIdToStr(obj):
    """
    digunakan untuk mengubah tipe pada 
    hasil mongoDB menjadi string
    yg bisa ditampilkan melalui FAST API

    mengubah ObjId jadi string saja
    """
    return str(obj["_id"])

def api_get_educational(**params):
    res = db.showEducationalById(**params)
    res["_id"] = objIdToStr(res)
    return res

def api_get_educationals():
    res = db.showEducational()
    data_list = []
    for educational in res:
        educational["_id"] = objIdToStr(educational)
        data_list.append(educational)
    return data_list

def api_delete_educational(**params):
    db.deleteEducationalById(**params)
    return {"message":"Delete educational data succeed"}

def api_edit_educational(**params):
    db.updateEducationalById(**params)
    return {"message":"educational data edited"}

def api_post_educational(**params):
    _logger.warning('TESS ',params)
    data = {
        "educational_id" :params['educational_id'],
        "tahunajaran" :params['tahunajaran'],
        "tingkat":params['tingkat']
    }
    db.insertEducational(data)
    return {"message":"educational data created"}



