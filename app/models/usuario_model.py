from pydantic import BaseModel
from typing import Optional

class User(BaseModel):     
    id: int= None
    id_rol: int
    cliente: str
    correo: str
    usuario_l:str
    password: str 
    jefe_de_uso: str 
    telefono: Optional[str] = None
    ciudad: Optional[str] = None
    direccion: Optional[str] = None
    nic: Optional[str] = None
    estado: bool

class Login(BaseModel):     
    correo: str
    password: str     

class User_id(BaseModel):     
    id: int      

class Actualizar(BaseModel):
    id: int= None
    cliente: str
    correo: str
    usuario_l:str
    password: str 
    jefe_de_uso: str 
    telefono: str = None
    ciudad: str = None
    direccion: str = None
    nic: str = None
    estado: bool 

