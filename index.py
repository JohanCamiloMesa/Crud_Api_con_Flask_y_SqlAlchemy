from app import app
from Utils.database import db
from Models.anime_model import anime, Category
from src.dbcreate import init_database

# Initialize database first
init_database()

# Create tables within application context if they don't exist
with app.app_context():
    try:
        # Intenta consultar la tabla de animes
        anime.query.first()
    except Exception:
        # Si hay error, significa que las tablas no existen
        db.create_all()
        print("Database tables created successfully!")
    else:
        print("Database tables already exist!")

if __name__ == "__main__":
    app.run(debug=True, port=5000)