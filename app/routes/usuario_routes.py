from fastapi import APIRouter
from app.controller.usuario_controller import *
from app.models.usuario_model import User, Login


router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_client")
async def create_client(user: User):
    rpta = nuevo_usuario.create_client(user)
    return rpta


@router.post("/login")
async def login(user: Login):
    rpta = nuevo_usuario.login(user)
    return rpta

@router.get("/get_clients")
async def get_clients():
    rpta = nuevo_usuario.get_clients()
    return rpta
#y ESO?

@router.put()
async def update_client(user: User):
    rpta= nuevo_usuario.update_client(user)
    return rpta