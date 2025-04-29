import json

# Cargar el JSON original
with open('red.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Inicializar los nuevos nodos y edges
new_nodes = []
new_edges = []

# Diccionario para almacenar las marcas (para no repetir nodos)
marca_nodes = {}

# Iterar sobre los nodos de productos
for product in data['nodes']:
    # Extraer el id del producto y la marca
    product_id = product['id']
    marca = product.get('marca', '').upper().strip()

    # Crear el nodo de marca si no existe
    if marca and f"{marca}" not in marca_nodes:
        marca_nodes[f"{marca}"] = {
            "id": f"{marca}",
            "type": "marca",
            "name": marca
        }

    # Agregar el producto como nodo
    new_nodes.append({
        "id": product_id,
        "type": "producto",
        "name": product["name"],
        "marca": marca,
        "nombre_vendedor": product["nombre_vendedor"],
        "link_vendedor": product["link_vendedor"],
        "descripcion": product["descripcion"],
        "especificacion": product["especificacion"],
        "imagenes": product["imagenes"],
        "url": product["url"],
        "precio_oferta": product["precio_oferta"],
        "precio": product["precio"]
    })

    # Crear el edge entre el producto y la marca
    if marca:
        new_edges.append({
            "source": product_id,
            "target": f"{marca}",
            "type": "marca"
        })

# Agregar los nodos de marca al array de nodos
new_nodes.extend(marca_nodes.values())

# Crear la estructura final
output_data = {
    "directed": False,
    "multigraph": True,
    "graph": {},
    "nodes": new_nodes,
    "links": new_edges
}

# Guardar el nuevo JSON
with open('productos.json', 'w') as f:
    json.dump(output_data, f, indent=2)

print("JSON reformateado guardado como 'productos.json'")
