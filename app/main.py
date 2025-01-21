from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.usuario_routes import router as user_router
from app.routes.maquina_routes import router as machine_router
from app.routes.os_routes import router as Os_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",  #
    "http://26.135.80.104:5173",  #
    "https://biovent.lat/","https://biovent-frontend.onrender.com/",
    "http://localhost:5173",  #
    "https://d458-2800-484-1789-2d00-a5c1-1230-199c-33b3.ngrok-free.app","https://4483-2800-484-1789-2d00-a5c1-1230-199c-33b3.ngrok-free.app"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user_router) 
app.include_router(machine_router) 
app.include_router(Os_router) 

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