# app/core/graph.py
import json
from pathlib import Path
from typing import Optional, Dict, List
from collections import defaultdict

import networkx as nx
from networkx.readwrite import json_graph
from networkx.exception import PowerIterationFailedConvergence

GRAPH_PATH = Path("database/productos.json")

class GraphManager:
    _instance = None
    graph: nx.DiGraph  # Pylance ya no se queja si lo inicializamos bien

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.graph = cls._load_graph()
        return cls._instance

    @staticmethod
    def _load_graph() -> nx.DiGraph:
        if GRAPH_PATH.exists():
            try:
                with open(GRAPH_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Aquí se especifica explícitamente el parámetro edges
                    return nx.node_link_graph(data,edges='links')  # Usa "links" si tu JSON tiene ese campo
            except (json.JSONDecodeError, OSError, TypeError) as e:
                print(f"[GraphManager] Error cargando el grafo: {e}")
        return nx.DiGraph()


    def save_graph(self) -> None:
        try:
            with open(GRAPH_PATH, "w", encoding="utf-8") as f:
                json.dump(json_graph.node_link_data(self.graph,edges='links'), f, indent=2)
        except OSError as e:
            print(f"[GraphManager] Error guardando el grafo: {e}")

    def add_edge(self, from_node: str, to_node: str) -> None:
        self.graph.add_edge(from_node, to_node)

    def add_node(self, node_id: str, **attrs) -> None:
        self.graph.add_node(node_id, **attrs)

    def get_size_nodes(self) -> int:
        return self.graph.number_of_nodes()

    async def get_pagerank(self, personalization: Optional[dict[str, float]] = None, top_n: Optional[int] = None) -> list[tuple[str, float]]:
        try:
            # Calcular el PageRank
            if top_n is None:
                top_n = self.get_size_nodes()
            pr = nx.pagerank(self.graph, personalization=personalization) if personalization else nx.pagerank(self.graph)
            
            # Obtener los top_n productos
            top_products = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:top_n]

            # Crear una lista con los productos completos
            enriched_results = []
            for product_id, rank in top_products:
                # Obtener el nodo completo usando el ID
                product_data = self.graph.nodes[product_id]
                enriched_results.append({
                    'id': product_id,
                    'rank': rank,
                    'precio': product_data.get('precio', None),
                    'name': product_data.get('name', None),
                    'imagenes': product_data.get('imagenes', []),
                    'marca': product_data.get('marca', None),
                    'link_vendedor': product_data.get('link_vendedor',None),
                    'nombre_vendedor': product_data.get('nombre_vendedor',None)                
                })

            return enriched_results
        except PowerIterationFailedConvergence:
            print("[GraphManager] PageRank no convergió.")
            return []
    
    async def get_recommendations(
        self,
        prefs: Dict[str, float],
        id_email: str,
        top_n: int = 30,
        recommendations_per_node: int = 5,
        same_brand_boost: float = 0.5  # Factor para reducir la influencia de los productos de la misma marca
    ) -> list[tuple[str, float]]:
        if not prefs:
            return await self.get_pagerank(top_n=top_n)

        try:
            pr_map = nx.pagerank(self.graph)  # Calcula el PageRank de todos los nodos
        except PowerIterationFailedConvergence:
            pr_map = {}

        expanded_prefs = defaultdict(float)
        sorted_prefs = sorted(prefs.items(), key=lambda x: x[1], reverse=True)  # Ordenar productos por preferencia
        recommendations = []

        # Para cada producto que le gusta al usuario
        for i, (node_id, weight) in enumerate(sorted_prefs):
            if node_id not in self.graph:
                continue

            # Prioriza los productos más queridos por el usuario
            priority_boost = 1.0 - (i / len(sorted_prefs))
            expanded_prefs[node_id] += weight * priority_boost  # Aumenta la preferencia del producto base

            # Obtén la marca del producto
            node_brand = self.graph.nodes[node_id].get('marca')
            
            # Busca otros productos de la misma marca
            same_brand_nodes = [
                (other_id, attrs)
                for other_id, attrs in self.graph.nodes(data=True)
                if other_id != node_id and attrs.get('marca') == node_brand
            ]

            # Ordena los productos de la misma marca por PageRank
            same_brand_nodes.sort(key=lambda x: pr_map.get(x[0], 0), reverse=True)

            # Para los productos de la misma marca, se les aplica el boost del PageRank y preferencia,
            # pero con un factor de reducción para no sobrecargar las recomendaciones.
            for neighbor_id, _ in same_brand_nodes[:recommendations_per_node]:
                neighbor_rank = pr_map.get(neighbor_id, 0)
                # Aquí usamos el mismo boost, pero ahora con el factor de reducción
                expanded_prefs[neighbor_id] += (weight * priority_boost * neighbor_rank) * same_brand_boost

            # Añadir las recomendaciones a la lista final
            recommendations.extend(
                [
                    (neighbor_id, expanded_prefs[neighbor_id])
                    for neighbor_id, _ in same_brand_nodes[:recommendations_per_node]
                ]
            )

        # Normaliza las preferencias totales para crear una personalización por usuario
        total = sum(expanded_prefs.values())
        personalization = {k: v / total for k, v in expanded_prefs.items()} if total > 0 else {}

        # Finalmente, devuelve las recomendaciones personalizadas basadas en PageRank
        return await self.get_pagerank(personalization=personalization, top_n=top_n)


# Instancia global lista pa' usar
G = GraphManager()
