from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.usuario_routes import router as user_router
from app.routes.maquina_routes import router as machine_router
from app.routes.os_routes import router as Os_router
from app.routes.cronograma_routes import router as Crono_router

app = FastAPI()

#origins = [
 #  "http://127.0.0.1:5173",  #
  #  "http://26.135.80.104:5173",  #
   # "http://localhost:5173",  #
    #"https://biovent-backend.onrender.com",
    #"https://4be4-2800-484-1789-2d00-c002-b156-6743-4ce4.ngrok-free.app "
#]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://biovent.lat",  # Dominio del frontend
        "http://localhost:5173",  # Para el desarrollo local
        "http://biovent-frontend.onrender.com",
        "www.biovent.lat",
        "https://4be4-2800-484-1789-2d00-c002-b156-6743-4ce4.ngrok-free.app ",
        # Si usas otro dominio
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user_router) 
app.include_router(machine_router) 
app.include_router(Os_router) 
app.include_router(Crono_router) 

"""

@app.route('/')
def home():
    return ('+page.svelte')

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Render asigna el puerto en la variable PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
"""