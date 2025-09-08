"""
Utilidad para inicialización automática de la base de datos.

Este módulo se encarga de verificar la existencia de la base de datos
y crearla automáticamente si no existe. Es ejecutado antes de inicializar
la aplicación Flask para asegurar que la infraestructura de datos esté lista.
"""

# Importaciones necesarias
import mysql.connector  # Conector nativo de MySQL para Python
from Config.db_config import user, password, host, database  # Credenciales de DB

"""
    Inicializa la base de datos MySQL si no existe.
    
    Esta función implementa un patrón de inicialización segura:
    1. Intenta conectar a la base de datos específica
    2. Si no existe, se conecta al servidor y la crea
    3. Maneja errores de conexión y limpia recursos apropiadamente
    
    Raises:
        mysql.connector.Error: Si hay problemas de conexión o permisos
"""

def init_database():
    try:
        # Primer intento: conectar directamente a la base de datos específica
        try:
            # Intentar conexión con la base de datos objetivo
            conn = mysql.connector.connect(
                host=host,              # Servidor MySQL (ej: localhost)
                user=user,              # Usuario de MySQL
                password=password,      # Contraseña del usuario
                database=database       # Base de datos específica
            )
            # Si llegamos aquí, la base de datos ya existe
            print(f"Database '{database}' already exists!")
            return  # Salir temprano si la DB ya existe
            
        except mysql.connector.Error as err:
            # Verificar si el error es específicamente "base de datos no existe"
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                # La base de datos no existe, procedemos a crearla
                
                # Conectar al servidor MySQL sin especificar base de datos
                conn = mysql.connector.connect(
                    host=host,          # Servidor MySQL
                    user=user,          # Usuario con permisos de creación
                    password=password   # Contraseña del usuario
                )
                
                # Crear cursor para ejecutar comandos SQL
                cursor = conn.cursor()
                
                # Crear la base de datos si no existe
                # IF NOT EXISTS previene errores si la DB se crea concurrentemente
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                
                print(f"Database '{database}' created successfully!")
            else:
                # Cualquier otro error de MySQL (permisos, conexión, etc.)
                raise

    except mysql.connector.Error as err:
        # Manejar y re-lanzar errores de MySQL con información útil
        print(f"Error: {err}")
        raise

    finally:
        # Limpieza de recursos: cerrar cursor y conexión si existen
        # Usar 'locals()' para verificar si las variables fueron creadas
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()