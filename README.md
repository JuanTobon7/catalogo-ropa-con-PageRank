# catalogo-ropa-con-PageRank
## Integración de Backend y Frontend

Este proyecto combina el poder de **Astro** para el frontend y **Python** para el backend, creando un catálogo de ropa que utiliza el algoritmo de **PageRank** para ordenar los productos según su relevancia.

### Arquitectura del Proyecto

- **Frontend con Astro**: Astro se encargó de la generación de páginas estáticas y la interfaz de usuario. Su enfoque en el rendimiento permitió una experiencia fluida para los usuarios.
- **Backend con Python**: Python se utilizó para implementar el algoritmo de PageRank y manejar la lógica del servidor, incluyendo el procesamiento de datos y la gestión de visitas.

### Desafíos Encontrados

Uno de los principales retos fue la gestión de cookies debido al rendering de Astro. Aunque Astro genera páginas estáticas, logramos implementar un sistema que registra las visitas entre productos, simulando un comportamiento dinámico. Esto fue clave para alimentar el algoritmo de PageRank y mejorar la experiencia del usuario.

### Funcionalidades Principales

1. **Catálogo Dinámico**: Los productos se ordenan automáticamente según su relevancia calculada por PageRank.
2. **Seguimiento de Visitas**: Se registra la interacción del usuario entre productos para ajustar el ranking.
3. **Integración Fluida**: La comunicación entre Astro y Python se logró mediante API REST, asegurando un flujo de datos eficiente.

### Cómo Ejecutar el Proyecto

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/catalogo-ropa-con-PageRank.git
    ```
2. Instala las dependencias del frontend:
    ```bash
    cd client
    npm install
    ```
3. Instala las dependencias del backend:
    ```bash
    cd API
    pip install -r requirements.txt
    ```
4. Inicia el servidor backend:
    ```bash
    fastapi dev server.py
    ```
5. Inicia el servidor frontend:
    ```bash
    npm run dev
    ```

### Conclusión

Este proyecto demuestra cómo combinar tecnologías modernas para crear aplicaciones web eficientes y dinámicas. A pesar de los desafíos técnicos, logramos integrar el backend y el frontend de manera efectiva, ofreciendo una solución robusta y escalable.
