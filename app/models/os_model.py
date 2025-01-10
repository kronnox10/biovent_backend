from pydantic import BaseModel


class OS (BaseModel):
    id:int=None
    id_propietario: int
    id_maquina:int
    descripcion: str
    tecnico: str=None
    fecha_solicitud: str
    estado: bool


class Find_Os(BaseModel):
    id_usuario: int

class OST(BaseModel):
    id:int=None
    id_tecnico:int=None

