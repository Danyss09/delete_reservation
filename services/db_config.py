import mysql.connector
import os
from dotenv import load_dotenv  # Importa dotenv para cargar las variables de entorno
# Cargar las variables de entorno desde el archivo .env
load_dotenv()
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )
