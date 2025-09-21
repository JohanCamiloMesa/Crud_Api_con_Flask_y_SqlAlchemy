"""
Servicio para el modelo User.

Este módulo contiene la lógica de negocio relacionada con usuarios,
incluyendo registro, autenticación y gestión de usuarios.
Actúa como intermediario entre los controladores y los repositorios.
"""

from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash
from Utils.database import db
import logging

# Configurar logging
logger = logging.getLogger(__name__)

class UserService:
    """
    Servicio para manejar la lógica de negocio de usuarios.
    
    Esta clase encapsula toda la lógica de negocio relacionada con usuarios,
    incluyendo validaciones, hasheo de contraseñas y operaciones de autenticación.
    """

    @staticmethod
    def register_user(username, password):
        """
        Registra un nuevo usuario en el sistema.
        
        Valida que el usuario no exista previamente, hashea la contraseña
        y crea el usuario en la base de datos.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña en texto plano
            
        Returns:
            User: Objeto usuario creado
            dict: Diccionario con error si el usuario ya existe
        """
        logger.info(f'Registrando usuario en servicio: {username}')
        
        # Validar si el usuario ya existe
        existing_user = UserRepository.get_by_username(username, db.session)
        if existing_user:
            logger.warning(f'Intento de registro con usuario existente: {username}')
            return {'error': 'Usuario ya existe', 'username': username}
        
        # Hashear la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password)
        
        # Crear el usuario
        user = UserRepository.create_user(username, hashed_password, db.session)
        logger.info(f'Usuario creado en servicio: {user.username} (ID: {user.id})')
        return user

    @staticmethod
    def authenticate(username, password):
        """
        Autentica un usuario verificando sus credenciales.
        
        Busca el usuario por nombre de usuario y verifica que la contraseña
        proporcionada coincida con la contraseña hasheada almacenada.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña en texto plano
            
        Returns:
            User: Objeto usuario si la autenticación es exitosa
            None: Si las credenciales son incorrectas
        """
        logger.info(f'Autenticando usuario en servicio: {username}')
        
        # Buscar el usuario
        user = UserRepository.get_by_username(username, db.session)
        
        # Verificar contraseña si el usuario existe
        if user and check_password_hash(user.password, password):
            logger.info(f'Autenticación exitosa en servicio: {username}')
            return user
        
        logger.warning(f'Autenticación fallida en servicio: {username}')
        return None

    @staticmethod
    def get_all_users():
        """
        Obtiene todos los usuarios del sistema.
        
        Returns:
            List[User]: Lista de todos los usuarios registrados
        """
        logger.info('Obteniendo todos los usuarios en servicio')
        users = UserRepository.get_all(db.session)
        logger.info(f'{len(users)} usuarios obtenidos en servicio')
        return users

    @staticmethod
    def get_user_by_id(user_id):
        """
        Obtiene un usuario por su ID.
        
        Args:
            user_id (int): ID del usuario a buscar
            
        Returns:
            User: Objeto usuario si se encuentra
            None: Si no se encuentra el usuario
        """
        logger.info(f'Obteniendo usuario por ID en servicio: {user_id}')
        user = UserRepository.get_by_id(user_id, db.session)
        if user:
            logger.info(f'Usuario encontrado en servicio: {user.username}')
        else:
            logger.warning(f'Usuario no encontrado en servicio: {user_id}')
        return user

    @staticmethod
    def validate_user_data(username, password):
        """
        Valida los datos de entrada para registro/login.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not username or not password:
            return False, "username y password son requeridos"
        
        if len(username) < 3:
            return False, "El nombre de usuario debe tener al menos 3 caracteres"
        
        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        
        return True, None