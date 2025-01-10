from fastapi import APIRouter
from app.controller.os_controller import *
from app.models.os_model import *


router = APIRouter()

nueva_os = os_controller()

@router.post("/get_osi")
async def get_osi(os_id: Find_Os):
    rpta = nueva_os.get_osi(os_id)
    return rpta

@router.post("/get_os")
async def get_os(os_id: Find_Os):
    rpta = nueva_os.get_os(os_id)
    return rpta

@router.put("/asignar_tecnico_os")
async def asignar_tecnico_os(os:OST):
    rpta= nueva_os.asignar_tecnico_os(os)
    return rpta