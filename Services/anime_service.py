"""
Servicios de lógica de negocio para la gestión de animes.

Este módulo contiene todas las funciones que manejan la lógica de negocio
relacionada con las operaciones CRUD de animes. Incluye validaciones,
transformaciones de datos y manejo de errores.
"""

# Importaciones necesarias
from Models.anime_model import anime  # Modelo de anime
from Utils.database import db  # Instancia de SQLAlchemy para transacciones
from flask import request  # Para acceder a los datos del formulario

"""
    Extrae los datos del anime desde el formulario HTTP.
    
    Esta función centraliza la extracción de datos del formulario,
    facilitando el mantenimiento y reutilización del código.
    
    Returns:
        dict: Diccionario con los datos del anime extraídos del formulario.
        Incluye: name, genre, year, type, status
"""

def get_anime_from_form():
    return {
        'name': request.form.get("name"),        # Nombre del anime
        'genre': request.form.get("genre"),      # Género del anime
        'year': request.form.get("year"),        # Año de lanzamiento
        'type': request.form.get("type"),        # Tipo (TV, Movie, etc.)
        'status': request.form.get("status")     # Estado (Completed, Ongoing, etc.)
    }


"""
    Crea un nuevo anime en la base de datos.
    
    Esta función maneja la creación completa de un anime, incluyendo:
    - Extracción de datos del formulario
    - Validación de campos obligatorios
    - Conversión de tipos de datos
    - Inserción en la base de datos
    - Manejo de errores
    
    Returns:
        tuple: (bool, str) - (éxito, mensaje)
            - True, mensaje_éxito si la operación fue exitosa
            - False, mensaje_error si ocurrió algún error
"""

def create_anime():
    try:
        # Extraer datos del formulario
        form_data = get_anime_from_form()
        
        # Validar que ningún campo esté vacío
        # all() retorna False si algún valor es None, '', 0, etc.
        if not all(form_data.values()):
            return False, "Todos los campos son obligatorios"
        
        # Convertir año a entero para validación y almacenamiento
        form_data['year'] = int(form_data['year'])
        
        # Crear nueva instancia del modelo anime con los datos del formulario
        anime_new = anime(**form_data)
        
        # Agregar el nuevo anime a la sesión de la base de datos
        db.session.add(anime_new)
        
        # Confirmar la transacción (guardar en la base de datos)
        db.session.commit()
        
        return True, "Anime agregado satisfactoriamente"
        
    except ValueError:
        # Error de conversión de año a entero
        return False, "El año debe ser un número válido"
    except Exception as e:
        # Cualquier otro error: revertir cambios y reportar error
        db.session.rollback()
        return False, "Error al guardar el anime"

"""
    Actualiza un anime existente en la base de datos.
    
    Args:
        id (int): ID del anime a actualizar
    
    Returns:
        tuple: (bool, str) - (éxito, mensaje)
            - True, mensaje_éxito si la operación fue exitosa
            - False, mensaje_error si ocurrió algún error
"""

def update_anime(id):
    try:
        # Extraer datos del formulario
        form_data = get_anime_from_form()
        
        # Validar que ningún campo esté vacío
        if not all(form_data.values()):
            return False, "Todos los campos son obligatorios"

        # Buscar el anime por ID
        anime_to_update = anime.query.get(id)
        if not anime_to_update:
            return False, "Anime no encontrado"

        # Convertir año a entero
        form_data['year'] = int(form_data['year'])
        
        # Actualizar todos los campos del anime
        # setattr permite establecer atributos dinámicamente
        for key, value in form_data.items():
            setattr(anime_to_update, key, value)
        
        # Confirmar los cambios en la base de datos
        db.session.commit()
        return True, "Anime actualizado satisfactoriamente"
        
    except ValueError:
        # Error de conversión de año
        return False, "El año debe ser un número válido"
    except Exception as e:
        # Cualquier otro error: revertir y reportar
        db.session.rollback()
        return False, "Error al actualizar el anime"

"""
    Elimina un anime de la base de datos.
    
    Args:
        anime_id (int): ID del anime a eliminar
    
    Returns:
        tuple: (bool, str) - (éxito, mensaje)
            - True, mensaje_éxito si la operación fue exitosa
            - False, mensaje_error si ocurrió algún error
"""

def delete_anime(anime_id):
    try:
        # Buscar el anime por ID
        anime_to_delete = anime.query.get(anime_id)
        if not anime_to_delete:
            return False, "Anime no encontrado"
        
        # Eliminar el anime de la sesión
        db.session.delete(anime_to_delete)
        
        # Confirmar la eliminación en la base de datos
        db.session.commit()
        return True, "Anime eliminado satisfactoriamente"
        
    except Exception as e:
        # En caso de error: revertir y reportar
        db.session.rollback()
        return False, "Error al eliminar el anime"