import mysql.connector
import os
from dotenv import load_dotenv # <-- 1. Importar la librería

# -----------------------------------------------------------
# 2. Cargar las variables del entorno (.env)
#    Se carga una sola vez al inicio del módulo.
# -----------------------------------------------------------
load_dotenv() 

# 3. Definir las variables LEÍDAS del archivo .env
#    Asegúrate de que los nombres ("DB_HOST", "DB_USER", etc.) coincidan con tu archivo .env
DB_HOST = os.getenv("DB_HOST") 
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_connection():
    try:
        connection = mysql.connector.connect(
            # 4. Usar las variables de ENTORNO en lugar de los valores fijos
            host=DB_HOST,         
            user=DB_USER,
            password=DB_PASSWORD,  
            database=DB_NAME
        )
        return connection
    except Exception as error:
        # Aquí puedes ver si falla por el archivo .env no cargado
        print("Error al conectar:", error)
        print(f"DEBUG DB_HOST: {DB_HOST}") # <-- LÍNEA DE AYUDA PARA VER SI CARGÓ LA VARIABLE
        return None

# Ya no necesitas el fragmento de código de abajo que mencionaste, ¡quítalo!
# DB_HOST = os.getenv("DB_HOST") 
# # ... y el resto de las variables 
# # ...