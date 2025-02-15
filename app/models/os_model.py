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

class Find_machine(BaseModel):
    id_machine:int

class Get_os(BaseModel):
    id: int

class OST(BaseModel):
    id:int=None
    id_tecnico: str = None

class OSUpdate(BaseModel):
    id: int
    id_maquina: int
    estado_machine: bool
    estado: bool

class pendiente_os (BaseModel):
    id: int=None
    id_os: int
    id_maquina_p: int
    id_propietario: int
    descripcion: str
    repuestos: str
    estado_p: str
    

class Osp_pendientes(BaseModel):
    osupdate: OSUpdate
    pendiente:pendiente_os

