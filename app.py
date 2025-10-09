from flask import Flask 
from Controller.animes_controller import animes
from Controller.user_controller import users
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

# Configure session lifetime - las sesiones durarán 24 horas
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta_super_segura_jwt_cambiar_en_produccion'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds= 3600)  # Token expira en 1 hora
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Refresh token expira en 30 días
jwt = JWTManager(app)

# Initialize SQLAlchemy with app
db.init_app(app)

# Register blueprints
app.register_blueprint(animes)
app.register_blueprint(users)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('animes.home'))