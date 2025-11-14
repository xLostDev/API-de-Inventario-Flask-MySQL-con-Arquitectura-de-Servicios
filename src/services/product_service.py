# src/services/product_service.py

from db import get_connection # Importamos la función de conexión segura

# -------------------------
# READ (Obtener todos)
# -------------------------
def get_all_products():
    try:
        connection = get_connection() 
        if connection is None:
            return {"error": "No se pudo conectar a la base de datos"}, 500

        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM productos" 
        cursor.execute(query)
        
        products = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return products
        
    except Exception as error:
        print(f"Error al obtener productos: {error}")
        return {"error": "Error interno al obtener los datos"}, 500

# -------------------------
# CREATE (Crear producto)
# -------------------------
def create_product(data):
    try:
        connection = get_connection()
        if connection is None:
            return {"error": "No se pudo conectar a la base de datos"}, 500

        cursor = connection.cursor()
        query = "INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)"
        values = (data['nombre'], data['descripcion'], data['precio'], data['cantidad'])
        
        cursor.execute(query, values)
        connection.commit() 
        new_id = cursor.lastrowid 
        
        cursor.close()
        connection.close()

        return {"id": new_id, "message": "Producto agregado correctamente"}
        
    except Exception as error:
        print(f"Error al crear producto: {error}")
        return {"error": "Error interno al crear el producto"}, 500

# -------------------------
# UPDATE (Actualizar producto)
# -------------------------
def update_product(product_id, data):
    try:
        connection = get_connection()
        if connection is None:
            return {"error": "No se pudo conectar a la base de datos"}, 500

        cursor = connection.cursor()
        query = "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, cantidad=%s WHERE id=%s"
        values = (data['nombre'], data['descripcion'], data['precio'], data['cantidad'], product_id)
        
        cursor.execute(query, values)
        connection.commit()
        
        rows_affected = cursor.rowcount
        
        cursor.close()
        connection.close()

        if rows_affected == 0:
            return {"error": "Producto no encontrado"}, 404
        
        return {"message": "Producto actualizado correctamente"}

    except Exception as error:
        print(f"Error al actualizar producto: {error}")
        return {"error": "Error interno al actualizar el producto"}, 500

# -------------------------
# DELETE (Eliminar producto)
# -------------------------
def delete_product(product_id):
    try:
        connection = get_connection()
        if connection is None:
            return {"error": "No se pudo conectar a la base de datos"}, 500

        cursor = connection.cursor()
        query = "DELETE FROM productos WHERE id=%s"
        
        cursor.execute(query, (product_id,))
        connection.commit()
        
        rows_affected = cursor.rowcount
        
        cursor.close()
        connection.close()
        
        if rows_affected == 0:
            return {"error": "Producto no encontrado"}, 404
        
        return {"message": "Producto eliminado correctamente"}

    except Exception as error:
        print(f"Error al eliminar producto: {error}")
        return {"error": "Error interno al eliminar el producto"}, 500