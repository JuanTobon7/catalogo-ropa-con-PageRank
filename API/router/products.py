from fastapi import APIRouter
from controllers.products import Productos

router = APIRouter()

router.get('/productos')(Productos.getProducts)
router.get('/productos/id/{product_id}')(Productos.getProductsById)