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
    estado: str 
    descripcion_e: str=None 