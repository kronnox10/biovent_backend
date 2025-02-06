from fastapi import APIRouter,  UploadFile, File, Form
from app.controller.cronograma_controller import *
from app.models.cronograma_model import *
from typing import Optional


router = APIRouter()

nuevo_cronograma = Cronogramacontroller()

@router.post("/create_machine")
async def create_day(crono: calendar):
    rpta = nuevo_cronograma.create_day(crono)
    return rpta
