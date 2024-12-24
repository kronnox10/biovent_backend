from pydantic import BaseModel

class User(BaseModel):     
    id: int= None
    id_rol: int
    usuario: str
    password: str 



class Login(BaseModel):     
    usuario: str
    password: str     