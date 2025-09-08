"""
Configuración y inicialización de SQLAlchemy.

Este módulo contiene la configuración de la instancia principal de SQLAlchemy
que será utilizada por toda la aplicación para interactuar con la base de datos.
"""

# Importar SQLAlchemy para Flask
from flask_sqlalchemy import SQLAlchemy

# Crear instancia global de SQLAlchemy
# Esta instancia será inicializada con la aplicación Flask en app.py
# y utilizada por todos los modelos para definir tablas y realizar consultas
db = SQLAlchemy()