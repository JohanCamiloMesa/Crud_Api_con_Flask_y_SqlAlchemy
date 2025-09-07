from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Utils.database import db

class anime(db.Model):
    __tablename__ = 'Animes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    genre = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)

class Category(db.Model):
    __tablename__ = 'Categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    anime_id = Column(Integer, ForeignKey('Animes.id'))
    animes = relationship('anime', backref='category')