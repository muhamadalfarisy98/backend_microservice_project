from warnings import resetwarnings
from fastapi import FastAPI
from fastapi import APIRouter
from controller.educational_controller import *
import logging
_logger = logging.getLogger(__name__)

#menginisiasi object router yg dipanggil pada main.py
router = APIRouter()

@router.get("/educational")
async def view_search_educational_id(params:dict):
    res = api_get_educational(**params)
    return res

@router.get("/educationals")
async def view_search_educationals():
    res = api_get_educationals()
    return res

@router.delete("/educational")
async def delete_educational_by_id(params:dict):
    res = api_delete_educational(**params)
    return res

@router.put("/educational")
async def edit_educational_by_id(params:dict):
    res = api_edit_educational(**params)
    return res

@router.post("/educational")
async def post_educational_by_id(params:dict):
    res = api_post_educational(**params)
    return res


