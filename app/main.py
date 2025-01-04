from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.usuario_routes import router as user_router
from app.routes.maquina_routes import router as machine_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",  # Tu frontend local
    "http://26.135.80.104:5173",  # Tu dirección pública
    "http://localhost:5173",  # Permitir desde tu dominio local
    "http://26.135.80.104:5173",

]
 #ya. que era?
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user_router) 
app.include_router(machine_router) 

"""

@app.route('/')
def home():
    return ('+page.svelte')"""

"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) """

#...
#