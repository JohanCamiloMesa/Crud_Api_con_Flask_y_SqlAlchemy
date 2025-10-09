"""
Punto de entrada principal de la aplicación.

Este archivo es responsable de inicializar la base de datos,
crear las tablas necesarias y ejecutar la aplicación Flask.
"""

# Importaciones necesarias
from app import app  # Instancia principal de Flask
from Utils.database import db  # Instancia de SQLAlchemy
from Models.anime_model import anime  # Modelos de base de datos
from src.dbcreate import init_database  # Función para inicializar la base de datos

# Inicializar la base de datos MySQL (crear DB si no existe)
init_database()

# Crear tablas dentro del contexto de la aplicación si no existen
with app.app_context():
    try:
        # Intentar consultar la tabla de animes para verificar si existe
        anime.query.first()
    except Exception:
        # Si hay error, significa que las tablas no existen, por lo que las creamos
        db.create_all()
        print("Database tables created successfully!")
    else:
        # Si no hay error, las tablas ya existen
        print("Database tables already exist!")

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Ejecutar la aplicación Flask en modo debug en el puerto 5000
    # debug=True permite recarga automática y mejor debugging
    app.run(debug=True, port=5000)