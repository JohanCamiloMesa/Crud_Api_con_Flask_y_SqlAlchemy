from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DB')

# Usar PyMySQL como driver y soportar variables de entorno
if user and password and host and database:
	DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}/{database}"
else:
	# fallback a conexión directa si no hay variables de entorno
	DATABASE_CONNECTION_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_CONNECTION_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)