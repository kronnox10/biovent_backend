from fastapi import APIRouter,  UploadFile, File, Form
from app.controller.cronograma_controller import *
from app.models.cronograma_model import *
from typing import Optional


router = APIRouter()

nuevo_cronograma = Cronogramacontroller()

@router.post("/create_cronogr")
async def create_day(crono: calendar):
    rpta = nuevo_cronograma.create_day(crono)
    return rpta

@router.post("/getcronobyuser")
async def getdaysbyuser(crono_user: cronouser):
    rpta = nuevo_cronograma.getdaysbyuser(crono_user)
    return rpta

@router.post("/cargue_masivo_cronograma")
async def cargue_masivo_crono(file: UploadFile = File(...),id_usuario: int = Form(...)):
    rpta = nuevo_cronograma.cargue_masivo_crono(file,id_usuario)  # Esto está bien
    return rpta
