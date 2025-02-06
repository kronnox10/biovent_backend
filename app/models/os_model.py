from pydantic import BaseModel
from typing import Optional

class OS (BaseModel):
    id:int=None
    id_propietario: int
    id_maquina:int
    descripcion: str
    tecnico: Optional[int] = None
    estado: bool


class Find_Os(BaseModel):
    id_usuario: int

class OST(BaseModel):
    id:int=None
    id_tecnico: str = None

class OSUpdate(BaseModel):
    id: int

