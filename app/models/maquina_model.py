from pydantic import BaseModel
from typing import Optional

class Machine(BaseModel):     
    id: int= None
    id_user: int
    nombre: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    serial: Optional[str] = None
    inventario: Optional[str] = None
    ubicacion: Optional[str] = None
    sede: str
    estado: bool 
    descripcion_e: Optional[str] = None

class Find_machine(BaseModel):
    id_usuario: int

class Machinima(BaseModel):
    id:int

class UpdateMachine(BaseModel):
    id: int= None
    nombre: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    serial: Optional[str] = None
    inventario: Optional[str] = None
    ubicacion: Optional[str] = None
    sede: str
    estado: bool 
    descripcion_e: Optional[str] = None

class machineon(BaseModel):
    id_usuario: int
    estado:bool