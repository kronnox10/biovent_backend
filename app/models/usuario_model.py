from pydantic import BaseModel

class User(BaseModel):     
    id: int= None
    id_rol: int
    cliente: str
    correo: str
    password: str 
    jefe_de_uso: str 
    telefono: str = None
    ciudad: str = None
    direccion: str = None
    nic: str = None
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
    password: str 
    jefe_de_uso: str 
    telefono: str = None
    ciudad: str = None
    direccion: str = None
    nic: str = None
    estado: bool 

