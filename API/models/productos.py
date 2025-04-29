from pydantic import BaseModel

class Productos(BaseModel):
    id: str
    name: str
    descripcion: str
    especificaciones: str
    imagenes: list[str]
    precio: float
