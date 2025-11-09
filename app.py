from flask import Flask 
from Controller.animes_controller import animes
from Controller.user_controller import users
from Controller.manga_controller import mangas
from Utils.database import db
from Config.db_config import DATABASE_CONNECTION_URI
from flask import redirect, url_for
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "mysecretkey"

# Configure session to be permanent and last longer
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # Sesión dura 7 días
app.config['SESSION_COOKIE_SECURE'] = False  # Cambiar a True en producción con HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_REFRESH_EACH_REQUEST'] = True  # Renovar sesión en cada petición

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta_super_segura_jwt_cambiar_en_produccion'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds= 3600)  # Token expira en 1 hora
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Refresh token expira en 30 días
jwt = JWTManager(app)

# Initialize SQLAlchemy with app
db.init_app(app)

# Middleware para mantener la sesión activa
@app.before_request
def make_session_permanent():
    """
    Asegura que la sesión se mantenga activa y permanente en cada petición.
    Previene que clics rápidos causen pérdida de sesión.
    """
    from flask import session
    if session.get('is_authenticated'):
        session.permanent = True

# Register blueprints
app.register_blueprint(animes)
app.register_blueprint(users)
app.register_blueprint(mangas)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('animes.home'))