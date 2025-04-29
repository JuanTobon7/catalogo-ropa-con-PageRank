from fastapi import Request, HTTPException
from models.user import User as UserModel
from typing import Optional
from services.products import ProductsService

class Productos:
    @staticmethod
    async def getProducts(top_n: Optional[int] = None):
        return await ProductsService.getProducts(top_n)
    
    @staticmethod
    async def getProductsById(product_id: int):
        return await ProductsService.getProductsById(product_id)