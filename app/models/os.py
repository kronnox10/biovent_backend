from pydantic import BaseModel


class OS (BaseModel):
    id:int
    id_propietario: int
    id_maquina:int
    descripcion: str
    id_tecnico: int
    fecha_solicitud: str
    estado: bool