from flask import Blueprint, render_template, request, redirect, url_for, flash
from Models.anime_model import anime
from Services.anime_service import (
    create_anime as service_create_anime,
    update_anime as service_update_anime,
    delete_anime as service_delete_anime
)

animes = Blueprint('animes', __name__)

@animes.route("/")
def home():
    animes_list = anime.query.all()
    return render_template("Index.html", animes=animes_list)

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
    
    return render_template("Directorio.html", 
                         animes=animes_list,
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
    
    # Provide empty filters to avoid template errors
    return render_template("Directorio.html", 
                         animes=animes_list, 
                         search_query=query,
                         filters={
                             'genre': '',
                             'year': '',
                             'type': '',
                             'status': '',
                             'order': 'default'
                         })

@animes.route("/new", methods=["POST"])
def add_anime():
    success, message = service_create_anime()
    flash(message, "success" if success else "error")
    return redirect(url_for('animes.home'))

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

    return render_template('Update.html', anime=anime_to_update)

@animes.route('/delete/<id>')
def delete_anime(id):
    success, message = service_delete_anime(id)
    flash(message, "success" if success else "error")
    return redirect(url_for('animes.directory'))