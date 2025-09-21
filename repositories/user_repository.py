"""
Repositorio para el modelo User.

Este módulo maneja las operaciones de acceso a datos para el modelo User,
siguiendo el patrón Repository para separar la lógica de acceso a datos
de la lógica de negocio.
"""

from sqlalchemy.orm import Session
from Models.user_model import User
import logging

# Configurar logging
logger = logging.getLogger(__name__)

class UserRepository:
    """
    Repositorio para manejar operaciones CRUD del modelo User.
    
    Esta clase encapsula todas las operaciones de acceso a datos
    relacionadas con usuarios, proporcionando una interfaz limpia
    para la capa de servicios.
    """
    
    @staticmethod
    def get_by_username(username, session: Session):
        """
        Busca un usuario por su nombre de usuario.
        
        Args:
            username (str): Nombre de usuario a buscar
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            User: Objeto usuario si se encuentra, None en caso contrario
        """
        logger.info(f'Buscando usuario en repositorio: {username}')
        user = session.query(User).filter_by(username=username).first()
        if user:
            logger.info(f'Usuario encontrado en repositorio: {username}')
        else:
            logger.warning(f'Usuario no encontrado en repositorio: {username}')
        return user

    @staticmethod
    def create_user(username, password, session: Session):
        """
        Crea un nuevo usuario en la base de datos.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña hasheada
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            User: Objeto usuario creado
        """
        logger.info(f'Creando usuario en repositorio: {username}')
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        logger.info(f'Usuario creado en repositorio: {username} (ID: {user.id})')
        return user

    @staticmethod
    def get_all(session: Session):
        """
        Obtiene todos los usuarios de la base de datos.
        
        Args:
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            List[User]: Lista de todos los usuarios
        """
        logger.info('Obteniendo todos los usuarios en repositorio')
        users = session.query(User).all()
        logger.info(f'{len(users)} usuarios obtenidos en repositorio')
        return users

    @staticmethod
    def get_by_id(user_id, session: Session):
        """
        Busca un usuario por su ID.
        
        Args:
            user_id (int): ID del usuario a buscar
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            User: Objeto usuario si se encuentra, None en caso contrario
        """
        logger.info(f'Buscando usuario por ID en repositorio: {user_id}')
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            logger.info(f'Usuario encontrado por ID en repositorio: {user.username}')
        else:
            logger.warning(f'Usuario no encontrado por ID en repositorio: {user_id}')
        return user