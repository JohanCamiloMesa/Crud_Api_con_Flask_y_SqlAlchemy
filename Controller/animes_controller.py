from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from Models.anime_model import anime, GenreCategory
from Services.anime_service import (
    create_anime as service_create_anime,
    update_anime as service_update_anime,
    delete_anime as service_delete_anime
)

animes = Blueprint('animes', __name__)

@animes.route("/")
def home():
    # Si el usuario está autenticado, redirigir al dashboard
    if session.get('is_authenticated') and session.get('user_id'):
        return redirect(url_for('users.dashboard'))
    
    # Si no está autenticado, mostrar la página de inicio
    animes_list = anime.query.all()
    genres = GenreCategory.query.all()
    return render_template("Index.html", animes=animes_list, genres=genres)

@animes.route("/directory")
def directory():
    # Get filter parameters
    genre_filter = request.args.get('genre', '')
    year_filter = request.args.get('year', '')
    type_filter = request.args.get('type', '')
    status_filter = request.args.get('status', '')
    order_filter = request.args.get('order', 'default')
    
    # Start with base query
    query = anime.query
    
    # Apply filters
    if genre_filter:
        query = query.filter(anime.genre.ilike(f'%{genre_filter}%'))
    if year_filter:
        try:
            year_int = int(year_filter)
            if 1900 <= year_int <= 2100:
                query = query.filter(anime.year == year_int)
        except ValueError:
            pass  # Ignore invalid year values
    if type_filter:
        query = query.filter(anime.type == type_filter)
    if status_filter:
        query = query.filter(anime.status == status_filter)
    
    # Apply ordering
    if order_filter == 'alphabetic':
        query = query.order_by(anime.name.asc())
    else:  # default
        query = query.order_by(anime.id.asc())
    
    animes_list = query.all()
    
    # CRÍTICO: Obtener información del usuario autenticado para validaciones de seguridad
    user = None
    if session.get('is_authenticated') and session.get('user_id'):
        from Services.user_service import UserService
        try:
            user = UserService.get_user_by_id(session.get('user_id'))
        except Exception as e:
            print(f"Error obteniendo usuario: {e}")
    
    return render_template("Directorio.html", 
                         animes=animes_list,
                         user=user,  # Pasar información del usuario
                         filters={
                             'genre': genre_filter,
                             'year': year_filter,
                             'type': type_filter,
                             'status': status_filter,
                             'order': order_filter
                         })

@animes.route("/search")
def search():
    query = request.args.get('query', '')
    if query:
        animes_list = anime.query.filter(anime.name.ilike(f'%{query}%')).all()
    else:
        animes_list = anime.query.all()
    
    # CRÍTICO: Obtener información del usuario autenticado para validaciones de seguridad
    user = None
    if session.get('is_authenticated') and session.get('user_id'):
        from Services.user_service import UserService
        try:
            user = UserService.get_user_by_id(session.get('user_id'))
        except Exception as e:
            print(f"Error obteniendo usuario: {e}")
    
    # Provide empty filters to avoid template errors
    return render_template("Directorio.html", 
                         animes=animes_list, 
                         search_query=query,
                         user=user,  # Pasar información del usuario
                         filters={
                             'genre': '',
                             'year': '',
                             'type': '',
                             'status': '',
                             'order': 'default'
                         })

@animes.route("/new", methods=["GET", "POST"])
def add_anime():
    if request.method == "GET":
        # Mostrar formulario para agregar anime
        if not session.get('is_authenticated'):
            flash('Debes iniciar sesión para agregar animes', 'error')
            return redirect(url_for('users.login_page'))
        
        # Usuario autenticado puede ver el formulario
        genres = GenreCategory.query.all()
        return render_template("Index.html", animes=[], genres=genres, show_form_only=True)
    
    # POST: Procesar formulario
    if not session.get('is_authenticated'):
        flash('Debes iniciar sesión para agregar animes', 'error')
        return redirect(url_for('users.login_page'))
    
    success, message = service_create_anime()
    flash(message, "success" if success else "error")
    return redirect(url_for('animes.directory'))

@animes.route("/update/<id>", methods=["GET", "POST"])
def update_anime(id):
    anime_to_update = anime.query.get(id)
    if not anime_to_update:
        flash("Anime no encontrado", "error")
        return redirect(url_for('animes.directory'))

    if request.method == "POST":
        success, message = service_update_anime(id)
        flash(message, "success" if success else "error")
        return redirect(url_for('animes.directory'))

    genres = GenreCategory.query.all()
    return render_template('Update.html', anime=anime_to_update, genres=genres)

@animes.route('/delete/<id>')
def delete_anime(id):
    # Redirect to authentication page instead of directly deleting
    flash("Para eliminar un anime, debes autenticarte con tu token JWT.", "error")
    return redirect(url_for('users.dashboard'))

@animes.route('/api/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def api_delete_anime(id):
    """
    Endpoint API protegido para eliminar anime con autenticación JWT
    """
    try:
        current_user_id = get_jwt_identity()
        print(f"API Delete: Usuario {current_user_id} intentando eliminar anime {id}")  # Debug
        
        success, message = service_delete_anime(id)
        print(f"API Delete: Resultado del servicio: {success}, {message}")  # Debug
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'deleted_by_user': current_user_id
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': message
            }), 400
            
    except Exception as e:
        print(f"API Delete: Excepción: {str(e)}")  # Debug
        return jsonify({
            'success': False,
            'message': f'Error de autenticación: {str(e)}'
        }), 401