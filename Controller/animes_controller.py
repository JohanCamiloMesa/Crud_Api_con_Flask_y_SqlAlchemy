"""
Controlador de rutas para la gestión de animes.

Este módulo contiene todas las rutas HTTP (endpoints) de la aplicación,
manejando las peticiones del usuario y coordinando entre la capa de servicios
y las vistas (templates). Implementa el patrón MVC como controlador.
"""

# Importaciones de Flask para manejo de rutas y respuestas HTTP
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Importación del modelo de datos
from Models.anime_model import anime

# Importación de servicios de lógica de negocio
from Services.anime_service import (
    create_anime as service_create_anime,    # Servicio para crear anime
    update_anime as service_update_anime,    # Servicio para actualizar anime
    delete_anime as service_delete_anime     # Servicio para eliminar anime
)

# Crear Blueprint para agrupar las rutas relacionadas con animes
# Un Blueprint permite modularizar la aplicación y organizar las rutas
animes = Blueprint('animes', __name__)

"""
    Página principal de la aplicación.
    
    Muestra la página de inicio con el formulario para agregar animes
    y lista todos los animes existentes.
    
    Returns:
        str: HTML renderizado de la página principal
"""

@animes.route("/")
def home():
    # Obtener todos los animes de la base de datos
    animes_list = anime.query.all()
    # Renderizar template pasando la lista de animes
    return render_template("Index.html", animes=animes_list)

"""
    Página de directorio con funcionalidad de filtrado.
    
    Permite filtrar animes por género, año, tipo, estado y aplicar ordenamiento.
    Maneja múltiples parámetros de consulta (query parameters) para crear
    una experiencia de filtrado flexible.
    
    Returns:
        str: HTML renderizado del directorio con animes filtrados
"""

@animes.route("/directory")
def directory():
    # Obtener parámetros de filtro desde la URL (query parameters)
    genre_filter = request.args.get('genre', '')      # Filtro por género
    year_filter = request.args.get('year', '')        # Filtro por año
    type_filter = request.args.get('type', '')        # Filtro por tipo
    status_filter = request.args.get('status', '')    # Filtro por estado
    order_filter = request.args.get('order', 'default')  # Ordenamiento
    
    # Iniciar con consulta base (todos los animes)
    query = anime.query
    
    # Aplicar filtros dinámicamente según los parámetros recibidos
    
    # Filtro por género (búsqueda insensible a mayúsculas/minúsculas)
    if genre_filter:
        query = query.filter(anime.genre.ilike(f'%{genre_filter}%'))
    
    # Filtro por año con validación de rango
    if year_filter:
        try:
            year_int = int(year_filter)
            # Validar que el año esté en un rango razonable
            if 1900 <= year_int <= 2100:
                query = query.filter(anime.year == year_int)
        except ValueError:
            # Ignorar valores de año inválidos silenciosamente
            pass
    
    # Filtro por tipo exacto
    if type_filter:
        query = query.filter(anime.type == type_filter)
    
    # Filtro por estado exacto
    if status_filter:
        query = query.filter(anime.status == status_filter)
    
    # Aplicar ordenamiento según la preferencia del usuario
    if order_filter == 'alphabetic':
        # Ordenar alfabéticamente por nombre (A-Z)
        query = query.order_by(anime.name.asc())
    else:  # 'default'
        # Ordenamiento por defecto: por ID (orden de inserción)
        query = query.order_by(anime.id.asc())
    
    # Ejecutar la consulta con todos los filtros aplicados
    animes_list = query.all()
    
    # Renderizar template pasando resultados y filtros actuales
    # Los filtros se pasan para mantener el estado en el formulario
    return render_template("Directorio.html", 
                        animes=animes_list,
                        filters={'genre': genre_filter, 
                                'year': year_filter,
                                'type': type_filter,
                                'status': status_filter,
                                'order': order_filter})

"""
    Funcionalidad de búsqueda de animes por nombre.
    
    Permite buscar animes que contengan una cadena específica en su nombre.
    Usa búsqueda insensible a mayúsculas y minúsculas.
    
    Returns:
        str: HTML renderizado con resultados de búsqueda
"""

@animes.route("/search")
def search():
    # Obtener término de búsqueda desde parámetros URL
    query = request.args.get('query', '')
    
    if query:
        # Buscar animes cuyo nombre contenga el término de búsqueda
        # ilike: insensible a mayúsculas, %: wildcard para búsqueda parcial
        animes_list = anime.query.filter(anime.name.ilike(f'%{query}%')).all()
    else:
        # Si no hay término de búsqueda, mostrar todos los animes
        animes_list = anime.query.all()
    
    # Reutilizar template de directorio con filtros vacíos
    # Esto mantiene la consistencia en la interfaz de usuario
    return render_template("Directorio.html", 
                        animes=animes_list, 
                        search_query=query,
                        filters={'genre': '',
                                'year': '',
                                'type': '',
                                'status': '',
                                'order': 'default'})

"""
    Endpoint para agregar un nuevo anime.
    
    Procesa el formulario de creación de anime utilizando el servicio
    correspondiente. Solo acepta peticiones POST por seguridad.
    
    Returns:
        Response: Redirección a la página principal con mensaje flash
"""

@animes.route("/new", methods=["POST"])
def add_anime():
    # Llamar al servicio de creación de anime
    success, message = service_create_anime()
    
    # Agregar mensaje flash para mostrar al usuario el resultado
    # La categoría determina el estilo visual del mensaje
    flash(message, "success" if success else "error")
    
    # Redireccionar a la página principal
    return redirect(url_for('animes.home'))

"""
    Endpoint para actualizar un anime existente.
    
    Maneja tanto la visualización del formulario de edición (GET)
    como el procesamiento de la actualización (POST/PUT).
    
    Args:
        id (str): ID del anime a actualizar
        
    Returns:
        Response: GET - formulario de edición, POST/PUT - redirección con mensaje
"""

@animes.route("/update/<id>", methods=["GET", "PUT"])
def update_anime(id):
    # Buscar el anime por ID
    anime_to_update = anime.query.get(id)
    
    # Verificar que el anime existe
    if not anime_to_update:
        flash("Anime no encontrado", "error")
        return redirect(url_for('animes.directory'))

    if request.method == "PUT":
        # Procesar actualización del anime
        success, message = service_update_anime(id)
        
        # Para peticiones AJAX/JavaScript (PUT), devolver JSON
        return jsonify({
            'success': success, 
            'message': message,
            'redirect_url': url_for('animes.directory')
        })

    # GET: Mostrar formulario de edición con datos actuales
    return render_template('Update.html', anime=anime_to_update)

"""
    Endpoint para eliminar un anime.
    
    Elimina un anime específico usando el método HTTP DELETE
    siguiendo las convenciones REST estrictas.
    
    Args:
        id (str): ID del anime a eliminar
        
    Returns:
        Response: Redirección al directorio con mensaje flash
"""

@animes.route('/delete/<id>', methods=["DELETE"])
def delete_anime(id):
    # Llamar al servicio de eliminación
    success, message = service_delete_anime(id)
    
    # Para peticiones DELETE via JavaScript, devolver JSON
    return jsonify({
        'success': success, 
        'message': message,
        'redirect_url': url_for('animes.directory')
    })