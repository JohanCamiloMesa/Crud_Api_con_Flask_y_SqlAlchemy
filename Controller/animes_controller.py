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
    animes_list = anime.query.all()
    return render_template("Directorio.html", animes=animes_list)

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

