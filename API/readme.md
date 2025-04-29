🧠 Sistema de Servicio con Perfilamiento de Cliente y Motor de Búsqueda (con uso de Colas)
Este proyecto implementa un sistema de información con control de acceso a usuarios, que ofrece servicios personalizados basados en sus intereses mediante un motor de búsqueda predictivo y gestión de prioridades a través del uso de colas. El sistema prioriza y actualiza dinámicamente resultados e imágenes publicitarias según el perfil del usuario usando el algoritmo híbrido Page Rank + SOR-JOR.

🚀 Tecnologías Usadas
Python 3.11

FastAPI - para crear el backend y exponer endpoints.

NetworkX - para el manejo de grafos y simulación de algoritmos Page Rank y SOR-JOR.

JSON - utilizado como formato de almacenamiento persistente y ligero.

Uvicorn - servidor ASGI para correr FastAPI.

📌 Funcionalidades
🔐 Login de usuario con perfilamiento.

🔍 Motor de búsqueda predictivo según historial y gustos (tipo Facebook, YouTube, Google).

⚙️ Algoritmos híbridos (PageRank + SOR-JOR) para ordenamiento dinámico de resultados.

🧾 Colas de prioridad para actualizar publicidad e imágenes según el usuario activo.

📁 Almacenamiento persistente en archivos .json para usuarios, resultados y logs.

🛠️ Estructura del Proyecto
├── API/
│   ├── server.py              # Punto de entrada de FastAPI
│   ├── models/              # Modelos de datos (Pydantic)
│   ├── services/            # Lógica del negocio, búsquedas, colas
│   ├── core/                # Algoritmos de ranking y perfilamiento
│   ├── controllers/         # Controladores para manejar las solicitudes y respuestas
│   ├── media/               # Archivos estáticos como imágenes y videos
│   ├── router/              # Definición de rutas y endpoints
│   └── database/                # Archivos JSON para usuarios, productos, logs
└── README.md
📦 Archivo `requirements.txt`
El archivo `requirements.txt` incluye las dependencias necesarias para ejecutar el proyecto. Asegúrate de instalar estas dependencias antes de ejecutar el sistema.

```plaintext
fastapi==0.95.2
uvicorn==0.22.0
networkx==3.1
pydantic==1.10.7
```

Para instalar las dependencias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```
📖 Descripción Técnica
Usuarios: acceden mediante login y son perfilados según gustos históricos.

Algoritmos:

PageRank: determina la relevancia general de los ítems.

SOR-JOR: ajusta el orden en función del perfil del usuario activo.

Colas de prioridad: gestionan qué elementos se actualizan primero.

La información usada fue extraida de falabella con fines educativos