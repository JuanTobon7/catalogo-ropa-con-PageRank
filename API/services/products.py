from core.graph import G
from typing import Optional

class ProductsService:
    @staticmethod
    async def getProducts(top_n: Optional[int] = None):
        result = await G.get_pagerank(top_n=top_n)
        return result
    @staticmethod
    async def getProductsById(producto_id: int):
        result = G.graph.nodes[str(producto_id)]
        if not result:
            return {'error': 'id invalido'}
        return result
       