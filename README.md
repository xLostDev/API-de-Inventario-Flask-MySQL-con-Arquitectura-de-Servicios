# inventario-python-mysql
API REST de inventario creada con Python, Flask y MySQL. CRUD completo con conexión real a base de datos.

API de Inventario con Python + Flask + MySQL

Este proyecto es una API REST completa para gestión de inventario, desarrollada con:

Python

Flask

MySQL

CRUD completo (Crear, Leer, Actualizar, Eliminar)

Buenas prácticas con rutas separadas y conexión modular

Ideal para mostrar habilidades de backend y manejo de base de datos relacional.

Características

✔ Registrar productos
✔ Listar productos
✔ Editar productos
✔ Eliminar productos
✔ Conexión real a MySQL
✔ Código organizado y limpio

Tecnologías utilizadas

Python 3

Flask

MySQL Connector

Postman (para pruebas)

Estructura del proyecto
inventario_python/
├── app.py
├── db.py
├── test_db.py
├── venv/
└── README.md

Endpoints de la API
➤ Agregar producto

POST /agregar
Body JSON:

{
  "nombre": "Teclado Mecánico",
  "precio": 120.50,
  "cantidad": 15
}

➤ Obtener productos

GET /productos

➤ Editar producto

PUT /editar/<id>
Body JSON:

{
  "nombre": "Mouse Gamer Pro",
  "precio": 45.99,
  "cantidad": 10,
  "descripcion": "Accesorio RGB"
}

➤ Eliminar producto

DELETE /eliminar/<id>

Probar la API

Ejecutar en consola con el entorno virtual activado:

python app.py


La API quedará disponible en:

http://127.0.0.1:5000


Pruebas recomendadas: Postman / Thunder Client / curl.

Autor

José Peña
Desarrollador Junior Backend
Python | Flask | MySQL
