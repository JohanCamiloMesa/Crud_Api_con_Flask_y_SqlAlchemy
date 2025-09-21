"""
Modelo de datos para la gestión de usuarios y autenticación.

Este módulo define la clase que representa la entidad Usuario en la base de datos
utilizando SQLAlchemy ORM, siguiendo la misma estructura que el modelo anime.
"""

# Importaciones de SQLAlchemy para definir columnas
from sqlalchemy import Column, Integer, String
from Utils.database import db  # Instancia de SQLAlchemy
import logging

# Configurar logging
logger = logging.getLogger(__name__)

class User(db.Model):
    """
    Modelo que representa un usuario en la base de datos.
    
    Esta clase define la estructura de la tabla 'Users' con todos los campos
    necesarios para almacenar información de autenticación de usuarios.
    
    Attributes:
        id (int): Identificador único del usuario (clave primaria)
        username (str): Nombre de usuario único (máximo 80 caracteres)
        password (str): Contraseña hasheada del usuario (máximo 255 caracteres)
    """
    
    # Nombre de la tabla en la base de datos
    __tablename__ = 'Users'
    
    # Definición de columnas
    # ID: Clave primaria autoincremental con índice para búsquedas rápidas
    id = Column(Integer, primary_key=True, index=True)
    
    # Nombre de usuario: Campo obligatorio y único con longitud máxima de 80 caracteres
    username = Column(String(80), unique=True, nullable=False)
    
    # Contraseña: Campo obligatorio para almacenar la contraseña hasheada
    password = Column(String(255), nullable=False)

    def __repr__(self):
        """
        Representación del objeto Usuario para debugging.
        
        Returns:
            str: Representación legible del usuario
        """
        logger.info(f'Representación de usuario solicitada: {self.username}')
        return f'<User {self.username}>'