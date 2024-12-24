from fastapi import APIRouter
from app.controller.usuario_controller import *
from app.models.usuario_model import User, Login


router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.post("/login")
async def login(user: Login):
    rpta = nuevo_usuario.login(user)
    return rpta
