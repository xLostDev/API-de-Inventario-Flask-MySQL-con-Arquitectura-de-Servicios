import mysql.connector
import os
from dotenv import load_dotenv 


load_dotenv() 


DB_HOST = os.getenv("DB_HOST") 
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_connection():
    try:
        connection = mysql.connector.connect(
           
            host=DB_HOST,         
            user=DB_USER,
            password=DB_PASSWORD,  
            database=DB_NAME
        )
        return connection
    except Exception as error:
    
        print("Error al conectar:", error)
        print(f"DEBUG DB_HOST: {DB_HOST}") 
        return None

