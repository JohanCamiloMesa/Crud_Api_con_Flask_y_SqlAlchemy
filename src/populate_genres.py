"""
Script para poblar la tabla GenreCategories con todos los géneros de anime.

Este script inserta todos los géneros especificados en la tabla GenreCategories
si no existen previamente. Es seguro ejecutarlo múltiples veces.
"""

import sys
import os

# Añadir el directorio padre al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils.database import db
from Models.anime_model import GenreCategory
from app import app  # Importar la instancia de la aplicación

def populate_genres():
    """
    Pobla la tabla GenreCategories con todos los géneros de anime disponibles.
    
    La función verifica si cada género ya existe antes de insertarlo,
    evitando duplicados y errores de inserción.
    """
    
    # Lista completa de géneros de anime
    genres = [
        "Acción",
        "Artes Marciales", 
        "Aventuras",
        "Carreras",
        "Ciencia Ficción",
        "Comedia",
        "Demencia",
        "Demonios",
        "Deportes",
        "Drama",
        "Ecchi",
        "Escolares",
        "Espacial",
        "Fantasía",
        "Harem",
        "Historico",
        "Infantil",
        "Josei",
        "Juegos",
        "Magia",
        "Mecha",
        "Militar",
        "Misterio",
        "Música",
        "Parodia",
        "Policía",
        "Psicológico",
        "Recuentos de la vida",
        "Romance",
        "Samurai",
        "Seinen",
        "Shoujo",
        "Shounen",
        "Sobrenatural",
        "Superpoderes",
        "Suspenso",
        "Terror",
        "Vampiros",
        "Yaoi",
        "Yuri"
    ]
    
    print("🎬 Iniciando población de géneros de anime...")
    
    # Usar contexto de aplicación
    with app.app_context():
        try:
            # Contar géneros existentes
            existing_count = GenreCategory.query.count()
            print(f"📊 Géneros existentes en BD: {existing_count}")
            
            # Insertar géneros que no existen
            new_genres = 0
            for genre_name in genres:
                # Verificar si el género ya existe
                existing_genre = GenreCategory.query.filter_by(name=genre_name).first()
                
                if not existing_genre:
                    # Crear nuevo género
                    new_genre = GenreCategory(name=genre_name)
                    db.session.add(new_genre)
                    new_genres += 1
                    print(f"➕ Agregando: {genre_name}")
                else:
                    print(f"⏭️  Ya existe: {genre_name}")
            
            # Confirmar cambios en la base de datos
            if new_genres > 0:
                db.session.commit()
                print(f"✅ {new_genres} nuevos géneros agregados exitosamente!")
            else:
                print("ℹ️  Todos los géneros ya estaban en la base de datos.")
            
            # Mostrar total final
            final_count = GenreCategory.query.count()
            print(f"📈 Total de géneros en BD: {final_count}")
            
        except Exception as e:
            # Revertir cambios en caso de error
            db.session.rollback()
            print(f"❌ Error al poblar géneros: {e}")
            raise
        finally:
            # Cerrar sesión de base de datos
            db.session.close()

if __name__ == "__main__":
    populate_genres()