"""
Modelos de datos para la aplicación de gestión de animes.

Este módulo define las clases que representan las entidades de la base de datos
utilizando SQLAlchemy ORM. Incluye el modelo principal 'anime' y el modelo
relacionado 'Category' para categorizar los animes.
"""

# Importaciones de SQLAlchemy para definir columnas y relaciones
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Utils.database import db  # Instancia de SQLAlchemy

"""
    Modelo que representa un anime en la base de datos.
    
    Esta clase define la estructura de la tabla 'Animes' con todos los campos
    necesarios para almacenar información básica de un anime.
    
    Attributes:
        id (int): Identificador único del anime (clave primaria)
        name (str): Nombre del anime (máximo 255 caracteres)
        genre (str): Género del anime (máximo 50 caracteres)
        year (int): Año de lanzamiento del anime
        type (str): Tipo de anime (TV, Movie, OVA, etc.)
        status (str): Estado del anime (Completed, Ongoing, etc.)
"""
class anime(db.Model):    
    # Nombre de la tabla en la base de datos
    __tablename__ = 'Animes'
    
    # Definición de columnas
    # ID: Clave primaria autoincremental con índice para búsquedas rápidas
    id = Column(Integer, primary_key=True, index=True)
    
    # Nombre del anime: Campo obligatorio con longitud máxima de 255 caracteres
    name = Column(String(255), nullable=False)
    
    # Género: Campo obligatorio para clasificar el anime (Acción, Drama, etc.)
    genre = Column(String(50), nullable=False)
    
    # Año: Campo obligatorio para indicar el año de lanzamiento
    year = Column(Integer, nullable=False)
    
    # Tipo: Campo obligatorio para el tipo de producción (TV, Movie, OVA, Special)
    type = Column(String(50), nullable=False)
    
    # Estado: Campo obligatorio para el estado actual (Completed, Ongoing, Upcoming)
    status = Column(String(50), nullable=False)

"""
    Modelo que representa una categoría de anime.
    
    Esta clase define una relación uno a muchos con el modelo anime,
    permitiendo que cada anime pueda tener múltiples categorías asociadas.
    
    Attributes:
        id (int): Identificador único de la categoría
        name (str): Nombre de la categoría
        anime_id (int): Clave foránea que referencia al anime
        animes: Relación con el modelo anime
    """

class Category(db.Model):    
    # Nombre de la tabla en la base de datos
    __tablename__ = 'Categories'
    
    # ID: Clave primaria autoincremental con índice
    id = Column(Integer, primary_key=True, index=True)
    
    # Nombre de la categoría: Campo obligatorio
    name = Column(String(255), nullable=False)
    
    # Clave foránea que establece la relación con la tabla Animes
    anime_id = Column(Integer, ForeignKey('Animes.id'))
    
    # Relación bidireccional con el modelo anime
    # 'backref' crea automáticamente un atributo 'category' en el modelo anime
    animes = relationship('anime', backref='category')