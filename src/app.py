from flask import Flask, request, jsonify 

# Importamos todas las funciones del servicio, no la conexión directa a la DB
from services.product_service import (
    get_all_products, 
    create_product, 
    update_product, 
    delete_product
)

app = Flask(__name__)

# -------------------------
# Ruta para listar productos (GET)
# -------------------------
@app.route('/productos', methods=['GET'])
def obtener_productos():
    # Llama al servicio para obtener los datos.
    result = get_all_products()
    
    # Manejamos el error que el servicio devuelve como una tupla ({"error":...}, 500)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1] 
    
    # Éxito: devolvemos la lista de productos
    return jsonify(result), 200

# -------------------------
# Ruta para agregar producto (POST)
# -------------------------
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.get_json()

    # Llama al servicio para crear el producto
    result = create_product(data) 

    # Maneja la respuesta (éxito o error)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1] 

    return jsonify(result), 201 # 201 Created

# -------------------------
# Ruta para actualizar datos (PUT)
# -------------------------
@app.route('/productos/<int:product_id>', methods=['PUT'])
def update_producto(product_id): 
    data = request.get_json()
    result = update_product(product_id, data) 
    
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
        
    return jsonify(result)

# -------------------------
# Ruta para eliminar producto (DELETE)
# -------------------------
@app.route('/productos/<int:product_id>', methods=['DELETE'])
def eliminar_producto(product_id):
    result = delete_product(product_id)
    
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
        
    return jsonify(result)


# -------------------------
# Arranque del servidor
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)