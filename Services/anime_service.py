from Models.anime_model import anime
from Utils.database import db
from flask import request

def get_anime_from_form():
    return {
        'name': request.form.get("name"),
        'genre': request.form.get("genre"),
        'year': request.form.get("year"),
        'type': request.form.get("type"),
        'status': request.form.get("status")
    }

def create_anime():
    try:
        form_data = get_anime_from_form()
        
        # Validar que ningún campo esté vacío
        if not all(form_data.values()):
            return False, "Todos los campos son obligatorios"
        
        # Convertir año a entero
        form_data['year'] = int(form_data['year'])
        
        anime_new = anime(**form_data)
        db.session.add(anime_new)
        db.session.commit()
        return True, "Anime agregado satisfactoriamente"
    except ValueError:
        return False, "El año debe ser un número válido"
    except Exception as e:
        db.session.rollback()
        return False, "Error al guardar el anime"

def update_anime(id):
    try:
        form_data = get_anime_from_form()
        
        # Validar que ningún campo esté vacío
        if not all(form_data.values()):
            return False, "Todos los campos son obligatorios"

        anime_to_update = anime.query.get(id)
        if not anime_to_update:
            return False, "Anime no encontrado"

        # Convertir año a entero
        form_data['year'] = int(form_data['year'])
        
        # Actualizar campos
        for key, value in form_data.items():
            setattr(anime_to_update, key, value)
        
        db.session.commit()
        return True, "Anime actualizado satisfactoriamente"
    except ValueError:
        return False, "El año debe ser un número válido"
    except Exception as e:
        db.session.rollback()
        return False, "Error al actualizar el anime"

def delete_anime(anime_id):
    try:
        anime_to_delete = anime.query.get(anime_id)
        if not anime_to_delete:
            return False, "Anime no encontrado"
        
        db.session.delete(anime_to_delete)
        db.session.commit()
        return True, "Anime eliminado satisfactoriamente"
    except Exception as e:
        db.session.rollback()
        return False, "Error al eliminar el anime"