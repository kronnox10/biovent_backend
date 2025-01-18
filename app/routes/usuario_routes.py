from fastapi import APIRouter
from app.controller.usuario_controller import *
from app.models.usuario_model import *


router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_client")
async def create_client(user: User):
    rpta = nuevo_usuario.create_client(user)
    return rpta

@router.post("/create_technical")
async def create_technical(user: User):
    rpta = nuevo_usuario.create_technical(user)
    return rpta


@router.post("/login")
async def login(user: Login):
    rpta = nuevo_usuario.login(user)
    return rpta


@router.get("/get_clients")
async def get_clients():
    rpta = nuevo_usuario.get_clients()
    return rpta


@router.post("/get_client")
async def post_client(user: User_id):
    rpta = nuevo_usuario.post_client(user)
    return rpta


@router.get("/get_tecnicos")
async def get_tecnicos():
    rpta = nuevo_usuario.get_tecnicos()
    return rpta


@router.put("/update_client")
async def update_client(user: Actualizar):
    rpta= nuevo_usuario.update_client(user)
    return rpta


@router.get("/get_technicals")
async def get_technicals():
    rpta = nuevo_usuario.get_technicals()
    return rpta


@router.post("/get_technical")
async def get_technical(tecnico: User_id):
    rpta = nuevo_usuario.get_technical(tecnico)
    return rpta
