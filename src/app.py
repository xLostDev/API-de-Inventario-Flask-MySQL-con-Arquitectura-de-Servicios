from flask import Flask, request
from db import get_connection

app = Flask(__name__)

# -------------------------
# Ruta para agregar producto
# -------------------------
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.get_json()

    nombre = data.get("nombre")
    precio = data.get("precio")
    cantidad = data.get("cantidad")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)",
        (nombre, precio, cantidad)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Producto agregado con éxito"}, 201


# -------------------------
# Ruta para listar productos
# -------------------------
@app.route('/productos', methods=['GET'])
def obtener_productos():
    conn = get_connection()
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}, 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    cursor.close()
    conn.close()

    return productos, 200


# -------------------------
# Ruta para actualizar datos
# -------------------------
@app.route('/editar/<int:id>', methods=['PUT'])
def editar_producto(id):
    data = request.get_json()

    nombre = data.get("nombre")
    precio = data.get("precio")
    cantidad = data.get("cantidad")
    descripcion = data.get("descripcion")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE productos 
        SET nombre=%s, precio=%s, cantidad=%s, descripcion=%s
        WHERE id=%s
    """, (nombre, precio, cantidad, descripcion, id))

    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": "Producto actualizado correctamente"}, 200


# -------------------------
# Ruta para eliminar producto
# -------------------------
@app.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"mensaje": f"Producto con id {id} eliminado correctamente"}, 200


# -------------------------
# Arranque del servidor
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
