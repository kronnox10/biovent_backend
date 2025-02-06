from pydantic import BaseModel
from typing import Optional

class calendar(BaseModel):
    id_usuario: int
    equipo: str
    enero: bool
    febrero: bool
    marzo: bool
    abril: bool
    mayo: bool
    junio: bool
    julio: bool
    agosto: bool
    septiembre: bool
    octubre: bool
    noviembre: bool
    diciembre: bool