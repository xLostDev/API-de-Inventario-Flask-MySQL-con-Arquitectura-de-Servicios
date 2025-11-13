import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",   # cambia si tu contraseña es diferente
            database="inventario_python"
        )
        return connection
    except Exception as error:
        print("Error al conectar:", error)
        return None
