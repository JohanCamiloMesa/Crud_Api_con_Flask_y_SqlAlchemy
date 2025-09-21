"""
Controlador para el modelo User.

Este módulo define los endpoints REST y de autenticación para usuarios,
incluyendo registro, login y gestión de usuarios. Sigue el mismo patrón
que el controlador de animes existente.
"""

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from Services.user_service import UserService
import logging

# Configurar logging
logger = logging.getLogger(__name__)

# Crear blueprint para las rutas de usuarios
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/register', methods=['POST'])
def register():
    """
    Registro de usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [username, password]
          properties:
            username:
              type: string
              example: usuario1
              description: Nombre de usuario único
            password:
              type: string
              example: "Secreta123!"
              description: Contraseña del usuario
    responses:
      201:
        description: Usuario registrado exitosamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: usuario1
            message:
              type: string
              example: Usuario registrado exitosamente
      400:
        description: Petición inválida
        schema:
          type: object
          properties:
            error:
              type: string
              example: "username y password son requeridos"
      409:
        description: Usuario ya existe
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Usuario ya existe"
      500:
        description: Error interno al registrar
        schema:
          type: object
          properties:
            error:
              type: string
              example: "No se pudo completar el registro"
    """
    try:
        # Obtener datos del request
        data = request.get_json() or {}
        username = data.get('username')
        password = data.get('password')
        
        # Validar datos de entrada
        is_valid, error_message = UserService.validate_user_data(username, password)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        logger.info(f'Registrando usuario: {username}')
        user = UserService.register_user(username, password)

        # Verificar si el registro fue exitoso
        if isinstance(user, dict) and user.get('error') == 'Usuario ya existe':
            logger.warning(f'Usuario ya existe: {username}')
            return jsonify({'error': 'Usuario ya existe'}), 409

        logger.info(f'Usuario registrado: {user.username} (ID: {user.id})')
        return jsonify({
            'id': user.id, 
            'username': user.username,
            'message': 'Usuario registrado exitosamente'
        }), 201

    except Exception as e:
        logger.exception("Error en registro de usuario")
        return jsonify({'error': 'No se pudo completar el registro', 'detail': str(e)}), 500


@users.route('/login', methods=['POST'])
def login():
    """
    Login de usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [username, password]
          properties:
            username:
              type: string
              example: usuario1
            password:
              type: string
              example: "Secreta123!"
    responses:
      200:
        description: Login exitoso y retorno de JWT
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
            user:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: usuario1
            message:
              type: string
              example: Login exitoso
      400:
        description: Petición inválida
        schema:
          type: object
          properties:
            error:
              type: string
              example: "username y password son requeridos"
      401:
        description: Credenciales inválidas
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Credenciales inválidas"
    """
    try:
        # Obtener datos del request
        data = request.get_json() or {}
        username = data.get('username')
        password = data.get('password')
        
        # Validar datos de entrada
        if not username or not password:
            return jsonify({"error": "username y password son requeridos"}), 400

        logger.info(f'Intento de login para usuario: {username}')
        user = UserService.authenticate(username, password)
        
        if user:
            # Crear token JWT
            access_token = create_access_token(identity=str(user.id))
            logger.info(f'Login exitoso para usuario: {username}')
            return jsonify({
                'access_token': access_token,
                'user': {
                    'id': user.id,
                    'username': user.username
                },
                'message': 'Login exitoso'
            }), 200

        logger.warning(f'Login fallido para usuario: {username}')
        return jsonify({'error': 'Credenciales inválidas'}), 401

    except Exception as e:
        logger.exception("Error en login de usuario")
        return jsonify({'error': 'Error interno en login', 'detail': str(e)}), 500


@users.route('/', methods=['GET'])
@jwt_required()
def get_users():
    """
    Listado de usuarios (requiere JWT)
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    responses:
      200:
        description: Listado de usuarios
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: usuario1
        examples:
          application/json:
            - id: 1
              username: usuario1
            - id: 2
              username: usuario2
      401:
        description: No autenticado
        schema:
          type: object
          properties:
            error:
              type: string
              example: "No autenticado"
            msg:
              type: string
              example: "Token inválido"
    """
    try:
        logger.info('Consultando listado de usuarios')
        users_list = UserService.get_all_users()
        logger.info(f'{len(users_list)} usuarios encontrados')
        return jsonify([{'id': u.id, 'username': u.username} for u in users_list]), 200
    except Exception as e:
        logger.error(f'Error al consultar usuarios: {str(e)}')
        return jsonify({'error': 'No autenticado', 'msg': str(e)}), 401


@users.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """
    Obtener perfil del usuario autenticado
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    responses:
      200:
        description: Datos del perfil del usuario
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: usuario1
      401:
        description: No autenticado
      404:
        description: Usuario no encontrado
    """
    try:
        # Obtener ID del usuario desde el token JWT
        current_user_id = get_jwt_identity()
        logger.info(f'Consultando perfil para usuario ID: {current_user_id}')
        
        user = UserService.get_user_by_id(int(current_user_id))
        if user:
            return jsonify({
                'id': user.id,
                'username': user.username
            }), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
            
    except Exception as e:
        logger.error(f'Error al consultar perfil: {str(e)}')
        return jsonify({'error': 'Error interno', 'detail': str(e)}), 500


# =========================
# Rutas para páginas web (interfaz de usuario)
# =========================

@users.route('/register-page', methods=['GET', 'POST'])
def register_page():
    """
    Página de registro de usuario con interfaz web.
    GET: Muestra el formulario de registro
    POST: Procesa el registro desde el formulario web
    """
    if request.method == 'GET':
        return render_template('Register.html')
    
    # POST: Procesar formulario de registro
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validar que las contraseñas coincidan
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('Register.html')
        
        # Validar datos
        is_valid, error_message = UserService.validate_user_data(username, password)
        if not is_valid:
            flash(error_message, 'error')
            return render_template('Register.html')

        logger.info(f'Registrando usuario desde web: {username}')
        user = UserService.register_user(username, password)

        # Verificar si el registro fue exitoso
        if isinstance(user, dict) and user.get('error') == 'Usuario ya existe':
            flash('El usuario ya existe', 'error')
            return render_template('Register.html')

        logger.info(f'Usuario registrado desde web: {user.username} (ID: {user.id})')
        flash(f'Usuario {user.username} registrado exitosamente', 'success')
        return redirect(url_for('users.login_page'))

    except Exception as e:
        logger.exception("Error en registro de usuario desde web")
        flash('Error interno al registrar usuario', 'error')
        return render_template('Register.html')


@users.route('/login-page', methods=['GET', 'POST'])
def login_page():
    """
    Página de login de usuario con interfaz web.
    GET: Muestra el formulario de login
    POST: Procesa el login desde el formulario web
    """
    if request.method == 'GET':
        return render_template('Login.html')
    
    # POST: Procesar formulario de login
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        
        if not username or not password:
            flash('Usuario y contraseña son requeridos', 'error')
            return render_template('Login.html')

        logger.info(f'Intento de login desde web para usuario: {username}')
        user = UserService.authenticate(username, password)
        
        if user:
            # Guardar información del usuario en la sesión
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_authenticated'] = True
            
            # Configurar sesión permanente si se seleccionó "recordarme"
            if remember_me:
                session.permanent = True
            
            logger.info(f'Login web exitoso para usuario: {username}')
            flash(f'¡Bienvenido {user.username}!', 'success')
            return redirect(url_for('users.dashboard'))

        logger.warning(f'Login web fallido para usuario: {username}')
        flash('Credenciales inválidas', 'error')
        return render_template('Login.html')

    except Exception as e:
        logger.exception("Error en login de usuario desde web")
        flash('Error interno en login', 'error')
        return render_template('Login.html')


@users.route('/dashboard')
def dashboard():
    """
    Dashboard del usuario autenticado.
    Muestra información del usuario y opciones disponibles.
    """
    # Verificar si el usuario está autenticado
    if not session.get('is_authenticated'):
        flash('Debes iniciar sesión para acceder al dashboard', 'error')
        return redirect(url_for('users.login_page'))
    
    try:
        user_id = session.get('user_id')
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('users.login_page'))
        
        return render_template('Dashboard.html', user=user)
    
    except Exception as e:
        logger.error(f'Error al cargar dashboard: {str(e)}')
        flash('Error al cargar dashboard', 'error')
        return redirect(url_for('users.login_page'))


@users.route('/logout')
def logout():
    """
    Cerrar sesión del usuario y limpiar tokens almacenados.
    """
    username = session.get('username', 'Usuario')
    
    # Limpiar la sesión
    session.clear()
    
    flash(f'¡Hasta luego {username}!', 'success')
    
    # Renderizar una página de logout que limpie el localStorage
    return render_template('Logout.html', redirect_url=url_for('animes.home'))


@users.route('/profile-page')
def profile_page():
    """
    Página de perfil del usuario (interfaz web).
    """
    # Verificar si el usuario está autenticado
    if not session.get('is_authenticated'):
        flash('Debes iniciar sesión para ver tu perfil', 'error')
        return redirect(url_for('users.login_page'))
    
    try:
        user_id = session.get('user_id')
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('users.login_page'))
        
        return render_template('Profile.html', user=user)
    
    except Exception as e:
        logger.error(f'Error al cargar perfil: {str(e)}')
        flash('Error al cargar perfil', 'error')
        return redirect(url_for('users.login_page'))


@users.route('/get-token')
def get_token():
    """
    Página para obtener el token JWT del usuario autenticado.
    """
    # Verificar si el usuario está autenticado
    if not session.get('is_authenticated'):
        flash('Debes iniciar sesión para obtener un token', 'error')
        return redirect(url_for('users.login_page'))
    
    try:
        user_id = session.get('user_id')
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('users.login_page'))
        
        # Crear token JWT para el usuario autenticado
        access_token = create_access_token(identity=str(user.id))
        
        logger.info(f'Token generado para usuario: {user.username}')
        flash('Token generado exitosamente', 'success')
        
        return render_template('Token.html', user=user, token=access_token)
    
    except Exception as e:
        logger.error(f'Error al generar token: {str(e)}')
        flash('Error al generar token', 'error')
        return redirect(url_for('users.dashboard'))