"""
Configuración de conexión a la base de datos.

Este módulo maneja toda la configuración relacionada con la conexión
a la base de datos MySQL, incluyendo el manejo de variables de entorno
para mayor seguridad y flexibilidad en diferentes entornos.
"""

# Importaciones necesarias
from dotenv import load_dotenv  # Para cargar variables de entorno desde .env
import os  # Para acceder a variables de entorno del sistema
from sqlalchemy.orm import sessionmaker  # Para crear sesiones de SQLAlchemy
from sqlalchemy import create_engine  # Para crear motor de base de datos

# Cargar variables de entorno desde archivo .env
# Esto permite configurar la aplicación sin hardcodear credenciales
load_dotenv()

# Extraer credenciales de base de datos desde variables de entorno
# Esto mejora la seguridad al no exponer credenciales en el código
user = os.getenv('MYSQL_USER')          # Usuario de MySQL
password = os.getenv('MYSQL_PASSWORD')  # Contraseña de MySQL
host = os.getenv('MYSQL_HOST')          # Host del servidor MySQL (ej: localhost)
database = os.getenv('MYSQL_DB')        # Nombre de la base de datos

# Construir URI de conexión a la base de datos
# Usar PyMySQL como driver y soportar variables de entorno
if user and password and host and database:
	# Si todas las variables están definidas, construir URI completa
	DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}/{database}"
else:
	# Fallback: usar URI directa si no hay variables de entorno individuales
	# Esto permite flexibilidad en la configuración
	DATABASE_CONNECTION_URI = os.getenv('DATABASE_URI')

# Crear motor de base de datos SQLAlchemy
# echo=True habilita logging de consultas SQL para debugging
engine = create_engine(DATABASE_CONNECTION_URI, echo=True)

# Crear factory de sesiones de SQLAlchemy
# autocommit=False: requiere commit manual para transacciones
# autoflush=False: requiere flush manual para enviar cambios pendientes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)