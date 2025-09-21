# Integración del Sistema de Autenticación

Este documento describe la integración del sistema de autenticación JWT en el proyecto Crud_Api_con_Flask_y_SqlAlchemy.

## Nuevas Funcionalidades Agregadas

### 1. Sistema de Autenticación JWT
- Registro de usuarios
- Login con generación de tokens JWT
- Protección de rutas con JWT
- Gestión de perfiles de usuario

### 2. Nuevas Dependencias
Se agregaron las siguientes dependencias en `requirements.txt`:
- `flask-jwt-extended`: Para manejo de tokens JWT
- `flasgger`: Para documentación automática con Swagger
- `pymysql`: Driver adicional para MySQL
- `PyYAML`: Para configuración de Swagger

### 3. Nuevos Archivos y Estructura

```
Models/
├── user_model.py          # Modelo de usuario para autenticación

repositories/
├── __init__.py
└── user_repository.py     # Repositorio para operaciones de datos de usuario

Services/
├── user_service.py        # Lógica de negocio para usuarios

Controller/
├── user_controller.py     # Endpoints de autenticación (REST API)

Config/
├── .env.example          # Plantilla de variables de entorno
```

### 4. Rutas Protegidas
Las siguientes rutas ahora requieren autenticación JWT:
- `POST /new` - Crear nuevo anime
- `PUT /update/<id>` - Actualizar anime
- `DELETE /delete/<id>` - Eliminar anime

### 5. Nuevos Endpoints de API

#### Autenticación
- `POST /users/register` - Registro de usuario
- `POST /users/login` - Login (retorna JWT token)
- `GET /users/` - Listar usuarios (requiere JWT)
- `GET /users/profile` - Perfil del usuario autenticado (requiere JWT)

#### API de Animes
- `GET /api/animes` - Obtener todos los animes (JSON)
- `GET /api/animes/<id>` - Obtener anime específico (JSON)

#### Utilidades
- `GET /health` - Health check
- `GET /api/info` - Información de la API

## Configuración

### 1. Variables de Entorno
Crea un archivo `.env` basado en `.env.example`:

```bash
# Configuración de la base de datos
DATABASE_URL=mysql://usuario:contraseña@localhost/nombre_base_datos

# Configuración JWT
JWT_SECRET_KEY=tu_clave_secreta_super_segura_aqui

# Configuración de la aplicación
FLASK_ENV=development
FLASK_DEBUG=True
```

### 2. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configuración de Base de Datos
El sistema creará automáticamente la tabla `Users` al iniciarse.

## Uso del Sistema de Autenticación

### 1. Registro de Usuario
```bash
curl -X POST http://localhost:5000/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "password123"}'
```

### 2. Login
```bash
curl -X POST http://localhost:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "password123"}'
```

Respuesta:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "usuario1"
  },
  "message": "Login exitoso"
}
```

### 3. Usar Token JWT
Para acceder a rutas protegidas, incluye el token en el header:
```bash
curl -X POST http://localhost:5000/new \
  -H "Authorization: Bearer tu_token_jwt_aqui" \
  -H "Content-Type: application/json" \
  -d '{"name": "Nuevo Anime", "genre": "Action", "year": 2024, "type": "TV", "status": "Ongoing"}'
```

## Documentación Swagger

La documentación interactiva de la API está disponible en:
- `http://localhost:5000/apidocs/`

## Características de Seguridad

1. **Contraseñas Hasheadas**: Las contraseñas se almacenan con hash seguro usando Werkzeug
2. **Tokens JWT**: Autenticación stateless con tokens JWT
3. **Validación de Datos**: Validación básica de entrada de datos
4. **Logging**: Registro detallado de operaciones de autenticación
5. **Manejo de Errores**: Respuestas JSON estructuradas para errores

## Compatibilidad

- ✅ **Rutas existentes preservadas**: Todas las rutas de animes existentes siguen funcionando
- ✅ **Templates preservados**: La interfaz web existente no se ve afectada
- ✅ **Base de datos compatible**: Se agregó la tabla Users sin afectar las existentes
- ✅ **Configuración flexible**: Soporta múltiples formas de configuración de BD

## Próximos Pasos Recomendados

1. **Configurar variables de entorno** en `.env`
2. **Instalar nuevas dependencias** con `pip install -r requirements.txt`
3. **Probar endpoints de autenticación** usando Swagger o curl
4. **Implementar autenticación en el frontend** si es necesario
5. **Configurar claves JWT más seguras** en producción

## Notas Importantes

- El sistema es **retrocompatible** con la funcionalidad existente
- Las rutas de lectura (GET) de animes **no requieren autenticación**
- Solo las operaciones de **modificación** (POST, PUT, DELETE) requieren JWT
- La documentación Swagger incluye ejemplos y esquemas completos