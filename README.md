
# ProyectoFinal_M6 – Autenticación en Django

Proyecto desarrollado como parte del **Módulo 6 – Desarrollo de Aplicaciones Web con Python Django**.  
El objetivo es implementar un sistema de autenticación de usuarios que incluya registro, inicio y cierre de sesión, además de vistas protegidas accesibles solo para usuarios autenticados.

---

## 📌 Funcionalidades implementadas

- Registro de usuarios mediante formulario.
- Inicio de sesión (login).
- Cierre de sesión (logout).
- Vista protegida (panel del usuario / dashboard).
- Redirección automática al login si un usuario no autenticado intenta acceder a una vista protegida.
- Uso de template base con herencia.
- Navegación dinámica según el estado de autenticación del usuario.
- Estilos básicos aplicados mediante CSS.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django
- HTML
- CSS
- Git / GitHub

---

## 📂 Estructura del proyecto

ProyectoFinal_M6/
│
├─ accounts/
│ ├─ migrations/
│ ├─ templates/
│ │ ├─ base.html
│ │ └─ accounts/
│ │ ├─ login.html
│ │ ├─ register.html
│ │ └─ dashboard.html
│ ├─ static/
│ │ └─ accounts/
│ │ └─ css/
│ │ └─ styles.css
│ ├─ views.py
│ ├─ forms.py
│ └─ urls.py
│
├─ ecommerce/
│ ├─ settings.py
│ ├─ urls.py
│ ├─ wsgi.py
│ └─ asgi.py
│
├─ screenshots/
│ ├─ registro.png
│ ├─ login.png
│ └─ dashboard.png
│
├─ manage.py
├─ README.md
└─ .gitignore

---

## 🔗 Rutas principales

- Registro de usuario: /register/
- Inicio de sesión: /login/
- Cierre de sesión: /logout/
- Vista protegida (Dashboard): /dashboard/

🔐 Vistas protegidas

La vista Dashboard está protegida mediante autenticación.
Si un usuario no autenticado intenta acceder directamente a /dashboard/, será redirigido automáticamente al login.

👤 Usuario de prueba

Los usuarios pueden crearse directamente desde la página de registro (/register/).
Una vez registrado, el usuario puede iniciar sesión y acceder al dashboard.

📸 Evidencia

- En la carpeta screenshots/ se incluyen capturas de:
- Registro de usuario.
- Inicio de sesión.

Acceso exitoso a la vista protegida (dashboard).

Alumna: Jeimy Caceres