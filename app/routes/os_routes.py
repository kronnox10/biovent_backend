from fastapi import APIRouter
from app.controller.os_controller import *
from app.models.os_model import *


router = APIRouter()

nueva_os = os_controller()

@router.post("/create_os")
async def create_os(os:OS):
    rpta = nueva_os.create_os(os)
    return rpta

@router.post("/get_osi")
async def get_osi(os_id: Find_Os):
    rpta = nueva_os.get_osi(os_id)
    return rpta

@router.post("/get_ost")
async def get_ost(os_id: Find_Os):
    rpta = nueva_os.get_ost(os_id)
    return rpta

@router.post("/get_osh")
async def get_osh(os_id: Find_Os):
    rpta = nueva_os.get_osh(os_id)
    return rpta

@router.get("/get_os_activas")
async def get_os_activas():
    rpta = nueva_os.get_os_activas()
    return rpta

@router.get("/get_historial_os")
async def get_historial_os():
    rpta = nueva_os.get_historial_os()
    return rpta

@router.post("/get_os")
async def get_os(os_id: Find_Os):
    rpta = nueva_os.get_os(os_id)
    return rpta

@router.put("/asignar_tecnico_os")
async def asignar_tecnico_os(os:OST):
    rpta= nueva_os.asignar_tecnico_os(os)
    return rpta

@router.post("/update_os")
async def update_os(osp_pendientes: Osp_pendientes):
    rpta= nueva_os.update_os(osp_pendientes)
    return rpta


@router.post("/get_pendientes")
async def get_pendientes(os_id: Find_Os):
    rpta= nueva_os.get_pendientes(os_id)
    return rpta

@router.post("/pendientes_pdf")
async def pendientes_pdf(Oss: Get_os):
    rpta= nueva_os.pendientes_pdf(Oss)
    return rpta


@router.post("/historial_os_machine")
async def historial_os_machine(HOS: Find_machine):
    rpta= nueva_os.historial_os_machine(HOS)
    return rpta