from fastapi import APIRouter,  UploadFile, File
from app.controller.maquina_controller import *
from app.models.maquina_model import *


router = APIRouter()

nueva_maquina = Machinecontroller()

@router.post("/create_machine")
async def create_machine(machine: Machine):
    rpta = nueva_maquina.create_machine(machine)
    return rpta
#voy
@router.post("/create_user_masivo")
async def cargue_masivo(file: UploadFile = File(...)):
    rpta = nueva_maquina.cargue_masivo(file)  # Esto está bien
    return rpta

@router.post("/get_machines")
async def get_machines(machine_id: Machinima):
    rpta = nueva_maquina.get_machines(machine_id)
    return rpta

@router.post("/get_machine")
async def get_machine(machine_id: Find_machine):
    rpta = nueva_maquina.get_machine(machine_id)
    return rpta
