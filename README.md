# 🎌 CRUD API con Flask y SQLAlchemy - Release v2.0

Una aplicación web completa para la gestión de animes con **sistema de autenticación JWT** desarrollada con Flask, SQLAlchemy y MySQL. Esta aplicación implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) con autenticación de usuarios, géneros dinámicos y una interfaz web moderna para administrar una base de datos de animes.

## 🆕 Novedades v2.0

- 🔐 **Sistema de Autenticación JWT completo**
- � **Registro y login de usuarios**
- 🛡️ **Protección de rutas con tokens**
- 🎬 **Géneros dinámicos desde base de datos**
- 📱 **Interfaz de usuario moderna**
- 🔗 **API REST con autenticación**
- 📚 **40+ géneros de anime predefinidos**

## �📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Sistema de Autenticación](#sistema-de-autenticación)
- [API Endpoints](#api-endpoints)
- [Base de Datos](#base-de-datos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## ✨ Características

### 🔐 Autenticación y Seguridad
- **Registro de usuarios** con validación completa
- **Login/Logout seguro** con JWT tokens
- **Dashboard personalizado** para cada usuario
- **Protección de rutas** con middleware JWT
- **Gestión de perfiles** de usuario
- **Sistema dual**: Autenticación web + API REST

### 🎬 Gestión de Animes
- **CRUD Completo**: Crear, leer, actualizar y eliminar animes
- **Géneros Dinámicos**: 40+ géneros cargados desde base de datos
- **Filtrado Avanzado**: Filtrar por género, año, tipo y estado
- **Ordenamiento**: Ordenar alfabéticamente o por ID
- **Búsqueda**: Sistema de búsqueda integrado
- **Autorización**: Solo usuarios autenticados pueden eliminar

### 🎨 Interfaz y UX
- **Interfaz Responsiva**: Diseño moderno con Bootstrap 5
- **Alertas Auto-ocultables**: Mensajes que desaparecen automáticamente
- **Navegación Intuitiva**: Barra de navegación contextual
- **Validación de Datos**: Validación tanto en frontend como backend
- **Manejo de Errores**: Gestión robusta de errores y mensajes informativos

## 🛠 Tecnologías Utilizadas

### Backend
- **Flask**: Framework web de Python
- **SQLAlchemy**: ORM para base de datos
- **Flask-SQLAlchemy**: Integración de SQLAlchemy con Flask
- **Flask-JWT-Extended**: Manejo de tokens JWT
- **Flasgger**: Documentación automática de API
- **MySQL**: Sistema de gestión de base de datos
- **python-dotenv**: Manejo de variables de entorno
- **Werkzeug**: Hashing de contraseñas
- **PyMySQL**: Conector MySQL optimizado

### Frontend
- **HTML5**: Estructura de páginas
- **Bootstrap 5**: Framework CSS moderno
- **Font Awesome**: Iconografía
- **JavaScript**: Interactividad y validaciones
- **Jinja2**: Motor de plantillas de Flask

### Base de Datos
- **MySQL**: Base de datos principal
- **Múltiples tablas**: Usuarios, Animes, Géneros
- **Relaciones optimizadas**: Foreign keys y índices

## 📁 Estructura del Proyecto

```
Crud_Api_con_Flask_y_SqlAlchemy/
├── app.py                          # Aplicación principal de Flask con JWT
├── index.py                        # Punto de entrada de la aplicación
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto
├── LICENSE                         # Licencia del proyecto
├── AUTH_INTEGRATION.md             # Documentación de autenticación
├── USER_INTERFACE_GUIDE.md         # Guía de interfaz de usuario
│
├── Config/                         # Configuraciones
│   └── db_config.py               # Configuración de base de datos
│
├── Controller/                     # Controladores (Rutas)
│   ├── animes_controller.py       # Controlador de animes
│   └── user_controller.py         # Controlador de usuarios (NUEVO)
│
├── Models/                         # Modelos de datos
│   ├── anime_model.py             # Modelo de anime y géneros
│   └── user_model.py              # Modelo de usuario (NUEVO)
│
├── Services/                       # Lógica de negocio
│   ├── anime_service.py           # Servicios de anime con géneros dinámicos
│   └── user_service.py            # Servicios de usuario (NUEVO)
│
├── repositories/                   # Capa de acceso a datos (NUEVO)
│   ├── __init__.py
│   └── user_repository.py         # Repositorio de usuarios
│
├── Templates/                      # Plantillas HTML
│   ├── Index.html                 # Página principal
│   ├── Layout.html                # Plantilla base
│   ├── Directorio.html            # Lista de animes con filtros dinámicos
│   ├── Search_results.html        # Resultados de búsqueda
│   ├── Update.html                # Formulario de actualización
│   ├── Dashboard.html             # Dashboard de usuario (NUEVO)
│   ├── Login.html                 # Página de login (NUEVO)
│   ├── Register.html              # Página de registro (NUEVO)
│   ├── Profile.html               # Perfil de usuario (NUEVO)
│   ├── Token.html                 # Gestión de tokens (NUEVO)
│   └── partials/                  # Componentes parciales
│       ├── _message.html          # Mensajes flash mejorados
│       ├── _navegationbar.html    # Barra de navegación con autenticación
│       └── _taskform.html         # Formulario con géneros dinámicos
│
├── Utils/                          # Utilidades
│   └── database.py                # Configuración de SQLAlchemy
│
└── src/                           # Scripts auxiliares
    ├── dbcreate.py                # Creación de base de datos
    └── populate_genres.py         # Poblado de géneros automático (NUEVO)
```

## 📋 Requisitos

### Requisitos del Sistema
- Python 3.7+
- MySQL 5.7+ o MariaDB
- pip (gestor de paquetes de Python)

### Dependencias Python
Las dependencias se encuentran listadas en `requirements.txt` e incluyen:

```
Flask>=2.3.0
Flask-SQLAlchemy>=3.0.0
Flask-JWT-Extended>=4.5.0
Flasgger>=0.9.7
python-dotenv>=1.0.0
Werkzeug>=2.3.0
PyMySQL>=1.1.0
```

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JohanCamiloMesa/Crud_Api_con_Flask_y_SqlAlchemy.git
cd Crud_Api_con_Flask_y_SqlAlchemy
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos MySQL

Asegúrate de tener MySQL instalado y ejecutándose en tu sistema.

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Configuración de MySQL
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=localhost
MYSQL_DB=animes_db

# Configuración JWT
JWT_SECRET_KEY=tu_clave_secreta_super_segura

# Alternativa: URI completa de base de datos
DATABASE_URI=mysql://usuario:contraseña@localhost/animes_db
```

### Configuración de Base de Datos

La aplicación creará automáticamente:
1. **Base de datos** si no existe
2. **Tablas necesarias** (Users, Animes, GenreCategories)
3. **Géneros predefinidos** (40+ géneros de anime)

### Inicialización Automática

Al ejecutar por primera vez:
```bash
python src/populate_genres.py  # Poblar géneros (opcional)
python index.py                # Iniciar aplicación
```

## 🎮 Uso

### Iniciar la aplicación

```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Iniciar aplicación
python index.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Funcionalidades Principales

#### 🔐 Sistema de Autenticación
1. **Registro** (`/register`): Crear nueva cuenta de usuario
2. **Login** (`/login`): Iniciar sesión con credenciales
3. **Dashboard** (`/dashboard`): Panel personal del usuario
4. **Profile** (`/profile`): Gestión de perfil de usuario
5. **Logout** (`/logout`): Cerrar sesión y limpiar tokens

#### 🎬 Gestión de Animes
1. **Página Principal** (`/`): Formulario para agregar nuevos animes (requiere autenticación)
2. **Directorio** (`/directory`): Lista completa con filtros dinámicos
3. **Búsqueda** (`/search`): Búsqueda avanzada por nombre
4. **Editar** (`/update/<id>`): Actualizar información
5. **Eliminar**: Eliminar con confirmación JWT (solo usuarios autenticados)

### 🎛️ Filtros Avanzados

- **Género**: 40+ géneros dinámicos desde base de datos
- **Año**: Filtro por año de lanzamiento (1900-2100)
- **Tipo**: TV, Movie, OVA, Special
- **Estado**: Completed, Ongoing, Upcoming
- **Ordenamiento**: Alfabético o por ID

## 🔐 Sistema de Autenticación

### Registro de Usuario
- Validación de email único
- Hash seguro de contraseñas con Werkzeug
- Campos: nombre, email, contraseña

### Login y JWT
- Autenticación con email/contraseña
- Generación de token JWT
- Almacenamiento en localStorage del navegador
- Expiración configurable de tokens

### Protección de Rutas
- Middleware JWT para rutas protegidas
- Verificación automática de tokens
- Redirección a login si no está autenticado

### Autorización
- Solo usuarios autenticados pueden:
  - Agregar nuevos animes
  - Eliminar animes existentes
- Funcionalidades públicas:
  - Ver directorio de animes
  - Buscar animes
  - Editar animes

## 🔗 API Endpoints

### 🔐 Autenticación (API REST)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/api/register` | Registro de usuario | No |
| POST | `/api/login` | Login y obtención de token | No |
| POST | `/api/logout` | Logout y revocación de token | JWT |

### 👤 Usuarios (Web Interface)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/register` | Página de registro | No |
| POST | `/register` | Procesar registro | No |
| GET | `/login` | Página de login | No |
| POST | `/login` | Procesar login | No |
| GET | `/dashboard` | Dashboard del usuario | Sesión |
| GET | `/profile` | Perfil del usuario | Sesión |
| POST | `/logout` | Cerrar sesión | Sesión |

### 🎬 Animes (Web + API)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/` | Página principal con formulario | No |
| POST | `/new` | Crear nuevo anime | JWT/Sesión |
| GET | `/directory` | Lista de animes con filtros | No |
| GET | `/search` | Búsqueda de animes | No |
| POST | `/search` | Procesar búsqueda | No |
| GET | `/update/<id>` | Formulario de edición | No |
| POST | `/update/<id>` | Actualizar anime | No |
| DELETE | `/delete/<id>` | Eliminar anime | JWT |

### � Géneros (API)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/api/genres` | Lista de todos los géneros | No |

### 📚 Documentación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/apidocs/` | Documentación Swagger UI |

## �🗃️ Base de Datos

### Tabla Users (NUEVA)

```sql
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla GenreCategories (NUEVA)

```sql
CREATE TABLE GenreCategories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);
```

### Tabla Animes (ACTUALIZADA)

```sql
CREATE TABLE Animes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL
);
```

### Géneros Predefinidos (40+ géneros)

```
Acción, Artes Marciales, Aventuras, Carreras, Ciencia Ficción, Comedia, 
Demencia, Demonios, Deportes, Drama, Ecchi, Escolares, Espacial, Fantasía, 
Harem, Historico, Infantil, Josei, Juegos, Magia, Mecha, Militar, Misterio, 
Música, Parodia, Policía, Psicológico, Recuentos de la vida, Romance, 
Samurai, Seinen, Shoujo, Shounen, Sobrenatural, Superpoderes, Suspenso, 
Terror, Vampiros, Yaoi, Yuri
```

### Campos del Modelo

#### User
- **id**: Identificador único (INTEGER, PRIMARY KEY)
- **name**: Nombre completo (STRING, NOT NULL)
- **email**: Email único (STRING, UNIQUE, NOT NULL)
- **password_hash**: Contraseña hasheada (STRING, NOT NULL)
- **created_at**: Fecha de creación (TIMESTAMP)

#### Anime
- **id**: Identificador único (INTEGER, PRIMARY KEY)
- **name**: Nombre del anime (STRING, NOT NULL)
- **genre**: Género del anime (STRING, NOT NULL)
- **year**: Año de lanzamiento (INTEGER, NOT NULL)
- **type**: Tipo de anime (STRING, NOT NULL)
- **status**: Estado del anime (STRING, NOT NULL)

#### GenreCategory
- **id**: Identificador único (INTEGER, PRIMARY KEY)
- **name**: Nombre del género (STRING, UNIQUE, NOT NULL)

## 🔧 Desarrollo

### Arquitectura del Sistema

#### Patrón MVC Implementado
- **Modelos** (`Models/`): Entidades de base de datos con SQLAlchemy
- **Vistas** (`Templates/`): Interfaces de usuario con Jinja2
- **Controladores** (`Controller/`): Lógica de rutas y endpoints

#### Capas de la Aplicación
1. **Presentación**: Templates HTML con Bootstrap 5
2. **Controladores**: Manejo de peticiones HTTP
3. **Servicios**: Lógica de negocio y validaciones
4. **Repositorios**: Acceso a datos (para usuarios)
5. **Modelos**: Definición de entidades
6. **Base de Datos**: MySQL con SQLAlchemy ORM

### Separación de Responsabilidades

#### Servicios (`Services/`)
- **anime_service.py**: CRUD de animes, géneros dinámicos
- **user_service.py**: Autenticación, registro, gestión de usuarios

#### Controladores (`Controller/`)
- **animes_controller.py**: Rutas para gestión de animes
- **user_controller.py**: Rutas para autenticación y usuarios

#### Repositorios (`repositories/`)
- **user_repository.py**: Acceso a datos de usuarios
- Patrón Repository para abstracción de datos

### Validaciones y Seguridad

#### Validaciones Implementadas
- **Frontend**: JavaScript + HTML5 validation
- **Backend**: Validación en servicios
- **Base de Datos**: Constraints y tipos de datos

#### Seguridad
- **Passwords**: Hash con Werkzeug (SHA-256 + salt)
- **JWT Tokens**: Tokens seguros con expiración
- **CORS**: Configuración de headers seguros
- **Input Validation**: Sanitización de entradas
- **SQL Injection**: Protección con SQLAlchemy ORM

### Nuevas Características v2.0

#### Géneros Dinámicos
- Migración de géneros hardcodeados a base de datos
- Script automático de población (`populate_genres.py`)
- Dropdowns dinámicos en todos los formularios
- 40+ géneros de anime predefinidos

#### Sistema de Autenticación
- JWT tokens para API REST
- Sesiones web para interfaz de usuario
- Middleware de autorización
- Dashboard personalizado

#### Mejoras de UI/UX
- Alertas auto-ocultables (4 segundos)
- Navegación contextual según autenticación
- Diseño responsive moderno
- Iconografía con Font Awesome

## 📖 Documentación Adicional

### Archivos de Documentación
- **AUTH_INTEGRATION.md**: Guía completa del sistema de autenticación
- **USER_INTERFACE_GUIDE.md**: Manual de la interfaz de usuario
- **README.md**: Documentación principal (este archivo)

### API Documentation
- **Swagger UI**: Disponible en `/apidocs/`
- **Endpoints**: Documentación automática con Flasgger
- **Schemas**: Definición de modelos de request/response

### Scripts Auxiliares
- **populate_genres.py**: Poblar géneros automáticamente
- **dbcreate.py**: Inicialización de base de datos
- Ejecutables independientemente para mantenimiento

## 🚀 Despliegue

### Desarrollo Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Poblar géneros (opcional)
python src/populate_genres.py

# Iniciar aplicación
python index.py
```

### Producción
1. **Configurar MySQL** en servidor
2. **Variables de entorno** seguras
3. **JWT_SECRET_KEY** robusto
4. **HTTPS** habilitado
5. **Servidor WSGI** (Gunicorn, uWSGI)

## 🧪 Testing

### Funcionalidades a Probar
- [ ] Registro de usuarios
- [ ] Login/Logout
- [ ] CRUD de animes
- [ ] Filtros dinámicos
- [ ] Autorización JWT
- [ ] Géneros dinámicos

### Datos de Prueba
- **Usuario**: test@example.com / password123
- **Géneros**: Cargados automáticamente
- **Animes**: Crear via interfaz web

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** el proyecto
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Áreas de Contribución
- 🔐 Mejoras de seguridad
- 🎨 Diseño y UX
- � Responsividad móvil
- 🧪 Tests unitarios
- 📖 Documentación
- 🌐 Internacionalización

### Estándares de Código
- **PEP 8** para Python
- **Comentarios** en español
- **Docstrings** descriptivos
- **Validaciones** robustas

## �📝 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Johan Camilo Mesa**
- 🌐 GitHub: [@JohanCamiloMesa](https://github.com/JohanCamiloMesa)
- 📧 Email: [Contacto](mailto:johancamilomesa@gmail.com)

## 🙏 Agradecimientos

- **Flask Community** por el excelente framework
- **SQLAlchemy** por el ORM robusto
- **Bootstrap** por los componentes UI
- **JWT** por la seguridad en tokens
- **MySQL** por la base de datos confiable

## 📊 Estadísticas del Proyecto

- **Líneas de código**: 2000+ líneas
- **Archivos**: 25+ archivos
- **Modelos**: 3 (User, Anime, GenreCategory)
- **Endpoints**: 15+ rutas
- **Templates**: 10+ páginas
- **Géneros**: 40+ predefinidos

## 🔄 Historial de Versiones

### v2.0.0 (Release Actual)
- ✅ Sistema de autenticación JWT completo
- ✅ Géneros dinámicos desde base de datos
- ✅ Interfaz de usuario moderna
- ✅ 40+ géneros predefinidos
- ✅ Documentación completa

### v1.0.0 (Versión Inicial)
- ✅ CRUD básico de animes
- ✅ Filtros hardcodeados
- ✅ Interfaz básica

---

⭐️ **Si este proyecto te fue útil, ¡dale una estrella en GitHub!**

📢 **¡Sígueme para más proyectos interesantes!**