"""
Archivo principal de configuración de la aplicación Flask.

Este módulo contiene la configuración principal de la aplicación web Flask,
incluyendo la configuración de la base de datos, inicialización de componentes
y registro de blueprints.
"""

# Importación de dependencias principales
from flask import Flask 
from Controller.animes_controller import animes  # Blueprint con las rutas de animes
from Utils.database import db  # Instancia de SQLAlchemy
from Config.db_config import DATABASE_CONNECTION_URI  # URI de conexión a la base de datos
from flask import redirect, url_for  # Utilidades para redirección

# Crear instancia principal de la aplicación Flask
app = Flask(__name__)

# Configuración de Flask-SQLAlchemy
# URI de conexión a la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
# Desactivar el seguimiento de modificaciones para mejorar el rendimiento
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Clave secreta para sesiones y mensajes flash (debería ser más segura en producción)
app.secret_key = "mysecretkey"

# Inicializar SQLAlchemy con la aplicación Flask
# Esto permite que db sea utilizado en otros módulos
db.init_app(app)

# Registrar blueprints (módulos de rutas)
# El blueprint 'animes' contiene todas las rutas relacionadas con la gestión de animes
app.register_blueprint(animes)

"""
Manejador personalizado para errores 404.
    
Args:
    e: El error 404 capturado
        
Returns:
    Redirección a la página principal de animes
"""
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('animes.home'))