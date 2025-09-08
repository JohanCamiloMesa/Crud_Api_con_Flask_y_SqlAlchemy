# 🎌 CRUD API con Flask y SQLAlchemy

Una aplicación web completa para la gestión de animes desarrollada con Flask, SQLAlchemy y MySQL. Esta aplicación implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) con una interfaz web intuitiva para administrar una base de datos de animes.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Base de Datos](#base-de-datos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## ✨ Características

- **CRUD Completo**: Crear, leer, actualizar y eliminar animes
- **Filtrado Avanzado**: Filtrar por género, año, tipo y estado
- **Ordenamiento**: Ordenar alfabéticamente o por ID
- **Búsqueda**: Sistema de búsqueda integrado
- **Interfaz Responsiva**: Diseño adaptable con Bootstrap
- **Validación de Datos**: Validación tanto en frontend como backend
- **Manejo de Errores**: Gestión robusta de errores y mensajes informativos
- **Configuración Flexible**: Soporte para variables de entorno

## 🛠 Tecnologías Utilizadas

### Backend
- **Flask**: Framework web de Python
- **SQLAlchemy**: ORM para base de datos
- **Flask-SQLAlchemy**: Integración de SQLAlchemy con Flask
- **MySQL**: Sistema de gestión de base de datos
- **python-dotenv**: Manejo de variables de entorno

### Frontend
- **HTML5**: Estructura de páginas
- **Bootstrap**: Framework CSS para diseño responsivo
- **Jinja2**: Motor de plantillas de Flask

### Base de Datos
- **MySQL**: Base de datos principal
- **mysql-connector-python**: Conector MySQL para Python

## 📁 Estructura del Proyecto

```
Crud_Api_con_Flask_y_SqlAlchemy/
├── app.py                          # Aplicación principal de Flask
├── index.py                        # Punto de entrada de la aplicación
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto
├── LICENSE                         # Licencia del proyecto
│
├── Config/                         # Configuraciones
│   └── db_config.py               # Configuración de base de datos
│
├── Controller/                     # Controladores (Rutas)
│   └── animes_controller.py       # Controlador de animes
│
├── Models/                         # Modelos de datos
│   └── anime_model.py             # Modelo de anime y categoría
│
├── Services/                       # Lógica de negocio
│   └── anime_service.py           # Servicios de anime
│
├── Templates/                      # Plantillas HTML
│   ├── Index.html                 # Página principal
│   ├── Layout.html                # Plantilla base
│   ├── Directorio.html            # Lista de animes
│   ├── Search_results.html        # Resultados de búsqueda
│   ├── Update.html                # Formulario de actualización
│   └── partials/                  # Componentes parciales
│       ├── _message.html          # Mensajes flash
│       ├── _navegationbar.html    # Barra de navegación
│       └── _taskform.html         # Formulario de anime
│
├── Utils/                          # Utilidades
│   └── database.py                # Configuración de SQLAlchemy
│
└── src/                           # Scripts auxiliares
    └── dbcreate.py                # Creación de base de datos
```

## 📋 Requisitos

### Requisitos del Sistema
- Python 3.7+
- MySQL 5.7+ o MariaDB
- pip (gestor de paquetes de Python)

### Dependencias Python
Las dependencias se encuentran listadas en `requirements.txt`:

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

# Alternativa: URI completa de base de datos
DATABASE_URI=mysql://usuario:contraseña@localhost/animes_db
```

### Configuración de Base de Datos

La aplicación creará automáticamente la base de datos y las tablas necesarias al ejecutarse por primera vez.

## 🎮 Uso

### Iniciar la aplicación

```bash
python index.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Funcionalidades Disponibles

1. **Página Principal** (`/`): Formulario para agregar nuevos animes
2. **Directorio** (`/directory`): Lista de todos los animes con opciones de filtrado
3. **Búsqueda** (`/search`): Búsqueda de animes por nombre
4. **Editar** (`/update/<id>`): Actualizar información de un anime
5. **Eliminar** (`/delete/<id>`): Eliminar un anime

### Filtros Disponibles

- **Género**: Filtro por género (ej: Acción, Drama, Comedia)
- **Año**: Filtro por año de lanzamiento
- **Tipo**: TV, Movie, OVA, Special
- **Estado**: Completed, Ongoing, Upcoming
- **Ordenamiento**: Alfabético o por ID

## 🔗 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Página principal con formulario |
| POST | `/add` | Crear nuevo anime |
| GET | `/directory` | Lista de animes con filtros |
| GET | `/search` | Búsqueda de animes |
| POST | `/search` | Procesar búsqueda |
| GET | `/update/<id>` | Formulario de edición |
| POST | `/update/<id>` | Actualizar anime |
| GET | `/delete/<id>` | Eliminar anime |

## 🗃️ Base de Datos

### Tabla Animes

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

### Tabla Categories (Relacional)

```sql
CREATE TABLE Categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    anime_id INT,
    FOREIGN KEY (anime_id) REFERENCES Animes(id)
);
```

### Campos del Modelo Anime

- **id**: Identificador único (INTEGER, PRIMARY KEY)
- **name**: Nombre del anime (STRING, NOT NULL)
- **genre**: Género del anime (STRING, NOT NULL)
- **year**: Año de lanzamiento (INTEGER, NOT NULL)
- **type**: Tipo de anime (STRING, NOT NULL)
- **status**: Estado del anime (STRING, NOT NULL)

## 🔧 Desarrollo

### Estructura de Código

1. **Modelos**: Define las entidades de base de datos usando SQLAlchemy
2. **Servicios**: Implementa la lógica de negocio y validaciones
3. **Controladores**: Maneja las rutas HTTP y la interacción con los servicios
4. **Templates**: Renderiza la interfaz de usuario con Jinja2

### Separación de Responsabilidades

- **Servicios** (`Services/`): Lógica de negocio
- **Configuración** (`Config/`): Configuraciones de la aplicación
- **Utilidades** (`Utils/`): Herramientas auxiliares

### Validaciones Implementadas

- Campos obligatorios
- Validación de tipos de datos
- Verificación de rangos de años
- Manejo de errores de base de datos

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Johan Camilo Mesa**
- GitHub: [@JohanCamiloMesa](https://github.com/JohanCamiloMesa)

---

⭐️ Si este proyecto te fue útil, ¡dale una estrella!