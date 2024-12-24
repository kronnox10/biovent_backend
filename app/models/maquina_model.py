from pydantic import BaseModel

class Machine(BaseModel):     
    id: int= None
    nombre: str
    serial: str 
    modelo: str 
    marca: str 
    inventario: str=None
    ubicacion: str 