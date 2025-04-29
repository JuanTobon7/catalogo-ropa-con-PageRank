from fastapi import FastAPI
from controllers.users import UserController
from router.users import router as router_user
from router.products import router as router_products
from router.interaction import router as router_interaction
from fastapi.staticfiles import StaticFiles
import os
from fastapi.middleware.cors import CORSMiddleware
# Configuración de CORS
origins = [
    "http://localhost:4321",
    "http://127.0.0.1:4321",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_user)
app.include_router(router_products)
app.include_router(router_interaction)
# Ruta al directorio 'falabella' dentro de la carpeta 'media'
media_path = os.path.join(os.path.dirname(__file__), 'media', 'falabella')

# Montar la ruta '/media/falabella' para que FastAPI sirva archivos desde 'server/media/falabella'
app.mount("/media/falabella", StaticFiles(directory=media_path), name="falabella")