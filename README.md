# 🎬 CRUD API con Flask y SQLAlchemy - Sistema Avanzado de Gestión de Animes

Una aplicación web completa y segura de gestión de animes desarrollada con Flask, SQLAlchemy y MySQL que incluye un **sistema JWT manual de dos pasos**, interfaz web moderna, API REST protegida y funcionalidades avanzadas de seguridad.

## ✨ Características Principales

### 🔐 **Sistema de Autenticación Avanzado**
- **JWT Manual de Dos Pasos**: Generación de token + Autenticación Manual obligatoria
- **Seguridad Individual por Usuario**: Cada usuario debe usar únicamente SUS propios tokens
- **Auto-Logout Inteligente**: Cierre automático de sesión al cerrar página/pestaña
- **Gestión de Múltiples Pestañas**: Manejo inteligente de sesiones en varias pestañas
- **Limpieza Automática**: LocalStorage se limpia automáticamente entre usuarios

### 🎨 **Interfaz de Usuario Moderna**
- **Dashboard Interactivo**: Panel personalizado con información de token en tiempo real
- **Modales Inteligentes**: Generación y autenticación de tokens en ventanas modales
- **Información de Token Dinámica**: Estado, duración, tiempo restante y autenticación
- **Gestión de Tokens**: Generar, verificar, eliminar y renovar tokens desde la interfaz
- **Responsive Design**: Interfaz adaptable con Bootstrap 5

### 🛡️ **Funcionalidades de Seguridad**
- **Validación Cruzada**: Verificación frontend y backend de propietario de tokens
- **Eliminación Segura de Animes**: Solo usuarios autenticados con SUS tokens pueden eliminar
- **Limpieza de Sesión**: Logout completo con limpieza de localStorage
- **Prevención de Uso Cruzado**: Tokens de otros usuarios automáticamente rechazados
- **Auditoría Completa**: Logs detallados de todas las operaciones de seguridad

### 🎬 **Gestión Completa de Animes**
- **CRUD Completo**: Crear, leer, actualizar y eliminar animes con autenticación
- **Filtros Avanzados**: Búsqueda por género, año, tipo, estado y nombre
- **Directorio Inteligente**: Vista optimizada con paginación y ordenamiento
- **Formulario Mejorado**: Validación en tiempo real y experiencia de usuario fluida

## 📋 Requisitos del Sistema

- Python 3.8+
- MySQL 5.7+ o MariaDB 10.3+
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/JohanCamiloMesa/Crud_Api_con_Flask_y_SqlAlchemy.git
   cd Crud_Api_con_Flask_y_SqlAlchemy
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   # En Windows
   .venv\Scripts\activate
   # En Linux/Mac
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   
   Crear un archivo `.env` en la raíz del proyecto:
   ```env
   MYSQL_USER=tu_usuario
   MYSQL_PASSWORD=tu_contraseña
   MYSQL_HOST=localhost
   MYSQL_DB=anime_db
   ```

5. **Crear la base de datos**
   ```sql
   CREATE DATABASE anime_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. **Ejecutar la aplicación**
   ```bash
   python index.py
   ```

La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
├── app.py                 # Configuración principal de Flask
├── index.py              # Punto de entrada de la aplicación
├── requirements.txt      # Dependencias del proyecto
├── Config/
│   └── db_config.py     # Configuración de base de datos
├── Controller/
│   ├── animes_controller.py    # Controlador de animes
│   └── user_controller.py      # Controlador de usuarios
├── Models/
│   ├── anime_model.py   # Modelo de datos de anime
│   └── user_model.py    # Modelo de datos de usuario
├── Services/
│   ├── anime_service.py # Lógica de negocio de animes
│   └── user_service.py  # Lógica de negocio de usuarios
├── repositories/
│   └── user_repository.py     # Capa de acceso a datos
├── Templates/           # Plantillas HTML
│   ├── Index.html
│   ├── Dashboard.html
│   ├── Login.html
│   └── ...
├── Utils/
│   └── database.py      # Configuración de SQLAlchemy
└── src/
    ├── dbcreate.py      # Inicialización de BD
    └── populate_genres.py # Datos iniciales
```

## 🔧 API Endpoints

### 🎬 **Animes**
- `GET /` - Página principal con lista de animes
- `GET /directory` - Directorio con filtros avanzados y paginación
- `GET /search` - Búsqueda de animes por nombre
- `GET /new` - Formulario para agregar anime (requiere autenticación)
- `POST /new` - Crear nuevo anime (requiere autenticación)
- `GET /update/<id>` - Formulario de edición (requiere autenticación)
- `POST /update/<id>` - Actualizar anime (requiere autenticación)
- `DELETE /api/delete/<id>` - Eliminar anime (requiere JWT válido)

### 👤 **Usuarios y Autenticación**
- `GET /users/register-page` - Página de registro
- `POST /users/register` - Registro de nuevo usuario
- `GET /users/login-page` - Página de login
- `POST /users/login` - Iniciar sesión web
- `POST /users/login` - API de login (JSON)
- `GET /users/dashboard` - Dashboard personalizado (requiere autenticación)
- `GET /users/logout` - Cerrar sesión con limpieza completa
- `POST /users/auto-logout` - Logout automático al cerrar página

### 🔐 **Sistema JWT Manual**
- `POST /users/generate-token` - Generar token JWT (requiere sesión activa)
- `GET /users/protected` - Verificar validez de token JWT
- `GET /users/token-status` - Estado detallado del token
- `POST /users/refresh` - Renovar token JWT
- `GET /users/token-page` - Página de gestión de tokens

### 🛡️ **Endpoints de Seguridad**
- `GET /users/profile-page` - Perfil de usuario
- `POST /users/validate-token` - Validar token manualmente
- `GET /users/` - Lista de usuarios (requiere JWT)

## 🎯 Guía de Uso Completa

### 👤 **1. Registro e Inicio de Sesión**
1. **Registrarse**: Accede a `/users/register-page` para crear una cuenta nueva
2. **Iniciar Sesión**: Usa `/users/login-page` con tus credenciales
3. **Dashboard**: Automáticamente redirige al dashboard personalizado

### 🔐 **2. Sistema JWT Manual (Paso a Paso)**

#### **Generar Token**
1. En el Dashboard, haz clic en **"Obtener Token"**
2. Se abre modal con tu token JWT personal (válido 1 hora)
3. **IMPORTANTE**: Generar token ≠ Estar autenticado

#### **Autenticarse Manualmente**
1. Haz clic en **"Autenticarse"** en el Dashboard
2. Pega tu token JWT en el modal de autenticación
3. El sistema verifica que el token sea **tuyo**
4. Solo entonces puedes eliminar animes

#### **Información de Token**
- **Duración**: Tiempo de expiración (1 hora)
- **Estado**: Activo/Expirado con tiempo restante
- **Autenticado**: Muestra si puedes eliminar animes

#### **Gestión de Tokens**
- **Verificar Estado**: Valida token contra el servidor
- **Eliminar Token**: Limpia completamente el token
- **Generar Nuevo**: Crea token fresco cuando expires

### 🎬 **3. Gestión de Animes**

#### **Ver y Explorar**
1. **Página Principal**: Vista general de todos los animes
2. **Directorio**: Filtros avanzados por género, año, tipo, estado
3. **Búsqueda**: Busca animes específicos por nombre

#### **Agregar Anime**
1. **Desde Dashboard**: Clic en "Agregar Anime"
2. **Llenar Formulario**: Nombre, género, año, tipo, estado
3. **Enviar**: Se guarda y redirige al directorio

#### **Eliminar Anime** (⚠️ Requiere Autenticación)
1. **Generar Token**: Obtén tu token JWT personal
2. **Autenticarse**: Valida tu token en el modal
3. **Eliminar**: Solo entonces puedes eliminar animes
4. **Seguridad**: Solo puedes usar TU propio token

### 🔒 **4. Características de Seguridad**

#### **Individual por Usuario**
- Cada usuario debe generar **SUS PROPIOS** tokens
- Tokens de otros usuarios son **automáticamente rechazados**
- Sistema verifica propietario del token

#### **Auto-Logout**
- Al cerrar página/pestaña → Sesión se cierra automáticamente
- Múltiples pestañas manejadas inteligentemente
- LocalStorage se limpia entre usuarios

#### **Limpieza de Sesión**
- Logout manual limpia **completamente** localStorage
- Nuevo usuario empieza con localStorage vacío
- Sin tokens residuales de usuarios anteriores

## 🔒 Sistema de Autenticación Avanzado

### 🎯 **JWT Manual de Dos Pasos**
El proyecto implementa un sistema de autenticación único con **Flask-JWT-Extended**:

#### **Paso 1: Generar Token**
- Usuario inicia sesión web normalmente
- Puede generar token JWT desde el Dashboard
- Token es personal e intransferible (contiene user_id)
- **Generar ≠ Estar Autenticado**

#### **Paso 2: Autenticación Manual**
- Usuario debe autenticarse manualmente con su token
- Pega token en modal de autenticación
- Sistema verifica propietario del token
- Solo entonces puede realizar operaciones críticas

### 🛡️ **Características de Seguridad**

#### **Validación Individual**
```javascript
// Frontend verifica propietario
if (tokenUserId !== currentUserId) {
    // Rechaza token de otro usuario
    alert('Token no válido para tu usuario');
    return;
}
```

#### **Backend Protegido**
```python
@jwt_required()
def api_delete_anime(id):
    current_user_id = get_jwt_identity()
    # Solo el propietario del token puede actuar
```

#### **Auto-Logout Inteligente**
- Event listener `beforeunload` detecta cierre de página
- `navigator.sendBeacon()` envía logout al servidor
- Limpieza automática de localStorage
- Gestión de múltiples pestañas

### ⏰ **Configuración de Tokens**
```python
# En app.py
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # 1 hora
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # 30 días

# En user_controller.py
'expires_in': 3600,  # 1 hora en segundos
```

### 🔄 **Flujo Completo de Seguridad**
1. **Login Web** → Sesión activa
2. **Generar Token** → Token personal creado
3. **Autenticación Manual** → Validación obligatoria
4. **Operaciones Críticas** → Solo con autenticación completa
5. **Auto-Logout** → Limpieza automática al cerrar página

## 🗄️ Modelos de Datos

### Anime
```python
- id: Integer (Primary Key)
- name: String(255)
- genre: String(50)
- year: Integer
- type: String(50)
- status: String(50)
```

### Usuario
```python
- id: Integer (Primary Key)
- username: String(80)
- password: String(255) # Hasheada
```

### Categorías de Género
```python
- id: Integer (Primary Key)
- name: String(100)
```

## 🚀 Despliegue y Configuración Avanzada

### **Variables de Entorno de Producción**
```env
# Configuración Flask
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=tu_clave_secreta_super_segura

# Base de Datos MySQL
MYSQL_USER=usuario_produccion
MYSQL_PASSWORD=contraseña_ultra_segura
MYSQL_HOST=tu_host_mysql
MYSQL_DB=anime_db_production
MYSQL_PORT=3306

# Configuración JWT
JWT_SECRET_KEY=clave_jwt_super_compleja_256_bits
JWT_ACCESS_TOKEN_EXPIRES=3600  # 1 hora
JWT_REFRESH_TOKEN_EXPIRES=2592000  # 30 días
```

### **Comandos de Despliegue Completo**
```bash
# 1. Clonar y configurar entorno
git clone <tu-repo>
cd Crud_Api_con_Flask_y_SqlAlchemy
python -m venv anime_env
source anime_env/bin/activate  # Linux/Mac
# O: anime_env\Scripts\activate  # Windows

# 2. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 3. Configurar base de datos
python src/dbcreate.py        # Crear tablas
python src/populate_genres.py # Poblar géneros

# 4. Verificar configuración
python -c "from app import app; print('✅ App configurada correctamente')"

# 5. Iniciar aplicación
# Desarrollo:
python index.py

# Producción (con Gunicorn):
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 index:app
```

### **Docker Deployment (Opcional)**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "index:app"]
```

### **Nginx Reverse Proxy**
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## � Testing y Calidad

### **Testing Manual con Postman**
```json
// Colección de endpoints para testing
{
  "endpoints": [
    "POST /users/api/token",        // Generar JWT
    "GET /users/token-status",      // Verificar token
    "POST /users/validate-token",   // Autenticación manual
    "DELETE /animes/api/1",         // Eliminar anime (requiere JWT)
    "GET /animes/search?q=naruto"   // Búsqueda de animes
  ]
}
```

### **Pruebas de Seguridad Recomendadas**
1. **Cross-User Token**: Verificar que tokens de otros usuarios sean rechazados
2. **Token Expiration**: Comprobar expiración de tokens (1 hora)
3. **Auto-logout**: Cerrar páginas y verificar limpieza de sesión
4. **SQL Injection**: Probar inputs maliciosos en formularios
5. **XSS Prevention**: Verificar escape de caracteres especiales

## 🤝 Contribuir al Proyecto

### **Guía de Contribución**
1. **Fork del Proyecto**
   ```bash
   git clone https://github.com/tu-usuario/Crud_Api_con_Flask_y_SqlAlchemy.git
   cd Crud_Api_con_Flask_y_SqlAlchemy
   ```

2. **Crear Rama de Feature**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # Ejemplos:
   # feature/admin-panel
   # bugfix/token-validation
   # security/rate-limiting
   ```

3. **Desarrollo y Testing**
   ```bash
   # Activar entorno virtual
   source anime_env/bin/activate
   
   # Instalar dependencias de desarrollo
   pip install pytest flask-testing
   
   # Ejecutar tests (si existen)
   python -m pytest tests/
   ```

4. **Commit con Estándares**
   ```bash
   git add .
   git commit -m "feat: agregar autenticación de dos factores"
   # Prefijos: feat, fix, docs, style, refactor, test, chore
   ```

5. **Push y Pull Request**
   ```bash
   git push origin feature/nueva-funcionalidad
   # Crear PR en GitHub con descripción detallada
   ```

### **Estándares de Código**
- **Python**: Seguir PEP 8
- **JavaScript**: Usar ES6+ y camelCase
- **HTML/CSS**: Indentación de 2 espacios
- **Comentarios**: Documentar funciones complejas
- **Commits**: Mensajes descriptivos en español/inglés

## 🌐 Stack Tecnológico Completo

### **Backend (Python)**
```python
Flask 3.0+           # Framework web principal
SQLAlchemy 2.0+      # ORM para base de datos avanzado
Flask-JWT-Extended   # Sistema JWT con validación individual
PyMySQL             # Conector MySQL optimizado
Werkzeug            # Utilidades web y seguridad
Python-dotenv       # Gestión de variables de entorno
```

### **Frontend (Moderno)**
```html
HTML5 Semántico     # Estructura web moderna
CSS3 + Grid/Flexbox # Diseño responsivo avanzado
Bootstrap 5.3       # Framework UI/UX profesional
JavaScript ES6+     # Interactividad y API calls
Jinja2 Templates    # Motor de plantillas dinámico
```

### **Base de Datos y Persistencia**
```sql
MySQL 8.0+          # Sistema de gestión relacional
Índices optimizados # Rendimiento en consultas
Foreign Keys        # Integridad referencial
Connection Pooling  # Gestión eficiente de conexiones
```

### **Seguridad Avanzada**
```python
JWT Individual      # Tokens únicos por usuario
CORS Configurado    # Política de origen cruzado
Session Management  # Gestión avanzada de sesiones
Auto-logout         # Limpieza automática inteligente
Input Validation    # Validación exhaustiva de entrada
Password Hashing    # Werkzeug security para contraseñas
```

### **Herramientas de Desarrollo**
```bash
Git                 # Control de versiones
Postman             # Testing de API endpoints
Chrome DevTools     # Debugging frontend
Python Virtual Env  # Aislamiento de dependencias
```

## � Roadmap y Mejoras Futuras

### **🔮 Próximas Características**
- [ ] **Admin Panel**: Dashboard administrativo con gestión de usuarios
- [ ] **Rate Limiting**: Protección contra spam y ataques DDoS
- [ ] **Email Verification**: Verificación por correo en registro
- [ ] **Two-Factor Authentication**: Autenticación de dos factores (2FA)
- [ ] **API Versioning**: Versionado de endpoints (/api/v1/, /api/v2/)
- [ ] **Logging Avanzado**: Sistema de logs estructurados
- [ ] **Cache Redis**: Cache para consultas frecuentes
- [ ] **WebSocket**: Notificaciones en tiempo real

### **🔧 Mejoras Técnicas Planificadas**
- [ ] **Unit Testing**: Suite completa de pruebas automatizadas
- [ ] **API Documentation**: Swagger/OpenAPI documentation
- [ ] **Performance Monitoring**: Métricas de rendimiento
- [ ] **Database Migration**: Sistema de migraciones automáticas
- [ ] **Docker Compose**: Orquestación completa con MySQL
- [ ] **CI/CD Pipeline**: GitHub Actions para deploy automático

## 📝 Licencia

```
MIT License

Copyright (c) 2024 Johan Camilo Mesa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 👨‍💻 Información del Desarrollador

### **Johan Camilo Mesa** 
🚀 **Full Stack Developer & Security Enthusiast**

```python
developer = {
    "name": "Johan Camilo Mesa",
    "role": "Full Stack Developer",
    "expertise": ["Python", "Flask", "JWT Security", "MySQL", "JavaScript"],
    "current_project": "Advanced JWT Authentication System",
    "github": "@JohanCamiloMesa",
    "specialization": "Web Security & API Development"
}
```

**Contacto:**
- 🔗 **GitHub**: [@JohanCamiloMesa](https://github.com/JohanCamiloMesa)
- 💼 **LinkedIn**: [Johan Camilo Mesa](https://linkedin.com/in/johancamilomesa)
- 📧 **Email**: johan.mesa@ejemplo.com
- 🌐 **Portfolio**: [johancamilomesa.dev](https://johancamilomesa.dev)

## 🐛 Reportar Issues y Soporte

### **🔍 Antes de Reportar**
1. **Busca issues existentes** en el repositorio
2. **Verifica la documentación** - puede ser una configuración
3. **Prueba en entorno limpio** - aislamiento de dependencias
4. **Revisa los logs** - pueden dar pistas del problema

### **📋 Template para Issues**
```markdown
## 🐛 Descripción del Bug
Descripción clara y concisa del problema.

## 🔄 Pasos para Reproducir
1. Ir a '...'
2. Hacer clic en '...'
3. Ver error

## ✅ Comportamiento Esperado
Lo que debería ocurrir normalmente.

## 📱 Entorno
- OS: [Windows/Linux/macOS]
- Browser: [Chrome/Firefox/Safari]
- Python Version: [3.11/3.12]
- Flask Version: [3.0+]

## 📸 Screenshots
Si aplica, adjunta capturas de pantalla.
```

### **💡 Sugerencias de Mejoras**
¿Tienes ideas para nuevas características? ¡Compártelas!
- Usa el template de **Feature Request**
- Explica el **caso de uso**
- Describe el **beneficio** para los usuarios

---

## 🏆 Reconocimientos

### **🙏 Agradecimientos Especiales**
- **Flask Community** - Por el excelente framework
- **Bootstrap Team** - Por el sistema de diseño
- **JWT.io** - Por la especificación JWT
- **MySQL Team** - Por el sistema de base de datos
- **Open Source Community** - Por inspiración y recursos

### **📚 Recursos y Referencias**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [JWT Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)

---

<div align="center">

### 🌟 **¿Te gustó el proyecto?**

Si este proyecto te ha sido útil, considera:

⭐ **Darle una estrella** en GitHub  
🍴 **Hacer un fork** para tus propios proyectos  
🐛 **Reportar bugs** que encuentres  
💡 **Sugerir mejoras** que te gustaría ver  
🤝 **Contribuir** con código  

---

**📢 Sígueme para más proyectos como este:**

[![GitHub](https://img.shields.io/badge/GitHub-JohanCamiloMesa-black?style=for-the-badge&logo=github)](https://github.com/JohanCamiloMesa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Johan_Camilo_Mesa-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/johancamilomesa)

---

### 🚀 **¡Construyamos el futuro del desarrollo web juntos!**

</div>