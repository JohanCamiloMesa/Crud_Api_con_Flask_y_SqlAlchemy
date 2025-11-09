from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from Services.manga_service import manga_api

mangas = Blueprint('mangas', __name__, url_prefix='/manga')

@mangas.route("/")
def manga_home():
    """Página principal de mangas"""
    return render_template("Manga_home.html")

@mangas.route("/browse")
def browse_manga():
    """Página para explorar mangas"""
    page = request.args.get('page', 1, type=int)
    genres = request.args.get('genres', '')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    # Obtener mangas de la API
    result = manga_api.fetch_manga(page=page, genres=genres if genres else None, 
                                   nsfw=nsfw, type_filter=type_filter)
    
    return render_template("Manga_browse.html", 
                         mangas=result.get('data', []),
                         error=result.get('error'),
                         page=page,
                         current_genres=genres,
                         current_type=type_filter,
                         current_nsfw=nsfw)

@mangas.route("/latest")
def latest_manga():
    """Página con los mangas más recientes"""
    page = request.args.get('page', 1, type=int)
    genres = request.args.get('genres', '')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    result = manga_api.fetch_latest(page=page, genres=genres if genres else None,
                                   nsfw=nsfw, type_filter=type_filter)
    
    return render_template("Manga_latest.html",
                         mangas=result.get('data', []),
                         error=result.get('error'),
                         page=page,
                         current_genres=genres,
                         current_type=type_filter,
                         current_nsfw=nsfw)

@mangas.route("/search")
def search_manga():
    """Búsqueda de mangas"""
    query = request.args.get('q', '')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    if not query:
        return render_template("Manga_search.html", mangas=[], query='')
    
    result = manga_api.search_manga(text=query, nsfw=nsfw, type_filter=type_filter)
    
    return render_template("Manga_search.html",
                         mangas=result.get('data', []),
                         error=result.get('error'),
                         query=query,
                         current_type=type_filter,
                         current_nsfw=nsfw)

@mangas.route("/detail/<manga_id>")
def manga_detail(manga_id):
    """Página de detalle de un manga"""
    manga_info = manga_api.get_manga(manga_id)
    chapters = manga_api.fetch_chapters(manga_id)
    
    if 'error' in manga_info:
        return render_template("Manga_detail.html", 
                             error=manga_info['error'],
                             manga=None,
                             chapters=[])
    
    return render_template("Manga_detail.html",
                         manga=manga_info.get('data'),
                         chapters=chapters.get('data', []),
                         error=chapters.get('error'))

@mangas.route("/chapter/<chapter_id>")
def manga_chapter(chapter_id):
    """Página para leer un capítulo"""
    images_data = manga_api.fetch_images(chapter_id)
    
    if 'error' in images_data:
        return render_template("Manga_reader.html",
                             error=images_data['error'],
                             images=[],
                             chapter_id=chapter_id)
    
    # La API devuelve 'data' como una lista de objetos con el campo 'link'
    data = images_data.get('data', [])
    
    # Extraer las URLs de las imágenes
    if isinstance(data, list):
        # Si es una lista, extraer el campo 'link' de cada objeto
        images = [item.get('link', item) if isinstance(item, dict) else item for item in data]
    else:
        # Si es un diccionario (formato alternativo), intentar obtener 'images'
        images = data.get('images', []) if isinstance(data, dict) else []
    
    return render_template("Manga_reader.html",
                         images=images,
                         chapter_info={'chapterNumber': chapter_id},
                         error=images_data.get('error'))

# API Endpoints (JSON responses)

@mangas.route("/api/fetch")
def api_fetch_manga():
    """API endpoint para obtener mangas"""
    page = request.args.get('page', 1, type=int)
    genres = request.args.get('genres')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    result = manga_api.fetch_manga(page=page, genres=genres, nsfw=nsfw, type_filter=type_filter)
    return jsonify(result)

@mangas.route("/api/latest")
def api_latest_manga():
    """API endpoint para obtener mangas recientes"""
    page = request.args.get('page', 1, type=int)
    genres = request.args.get('genres')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    result = manga_api.fetch_latest(page=page, genres=genres, nsfw=nsfw, type_filter=type_filter)
    return jsonify(result)

@mangas.route("/api/search")
def api_search_manga():
    """API endpoint para buscar mangas"""
    query = request.args.get('q', '')
    type_filter = request.args.get('type', 'all')
    nsfw = request.args.get('nsfw', 'true') == 'true'
    
    if not query:
        return jsonify({"error": "Se requiere un texto de búsqueda"}), 400
    
    result = manga_api.search_manga(text=query, nsfw=nsfw, type_filter=type_filter)
    return jsonify(result)

@mangas.route("/api/detail/<manga_id>")
def api_manga_detail(manga_id):
    """API endpoint para obtener detalle de un manga"""
    result = manga_api.get_manga(manga_id)
    return jsonify(result)

@mangas.route("/api/chapters/<manga_id>")
def api_manga_chapters(manga_id):
    """API endpoint para obtener capítulos de un manga"""
    result = manga_api.fetch_chapters(manga_id)
    return jsonify(result)

@mangas.route("/api/images/<chapter_id>")
def api_chapter_images(chapter_id):
    """API endpoint para obtener imágenes de un capítulo"""
    result = manga_api.fetch_images(chapter_id)
    return jsonify(result)
