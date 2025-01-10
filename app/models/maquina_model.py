from pydantic import BaseModel

class Machine(BaseModel):     
    id: int= None
    id_user: int
    nombre: str
    marca: str 
    modelo: str 
    serial: str 
    inventario: str=None
    ubicacion: str 
    estado: bool 
    descripcion_e: str=None 

class Find_machine(BaseModel):
    id_usuario: int

class Machinima(BaseModel):
    id:int

class UpdateMachine(BaseModel):
    id: int= None
    nombre: str
    marca: str 
    modelo: str 
    serial: str 
    inventario: str=None
    ubicacion: str 
    estado: bool 
    descripcion_e: str=None 