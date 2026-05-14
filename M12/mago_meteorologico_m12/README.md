El templado de un proyecto profesional

asistente_ventas/
├── .github/                # Automatización (CI/CD)
├── documentos/             # Documentación detallada del diseño
├── src/                    # Código fuente (El "corazón")
│   └── asistente_ventas/   # El paquete principal
│       ├── __init__.py     # Indica que esto es un módulo
│       ├── principal.py    # Punto de entrada (main.py)
│       ├── motor.py        # Lógica de procesamiento
│       └── utilidades.py   # Funciones de apoyo
├── pruebas/                # Tests para asegurar que nada explote
│   ├── __init__.py
│   ├── test_motor.py
│   └── test_interfaz.py
├── .gitignore              # Archivos que Git debe ignorar
├── pyproject.toml          # Configuración maestra del proyecto
├── LEEME.md                # El README.md (Explicación del proyecto)
└── requisitos.txt          # Librerías necesarias para que funcione


# Cosas nuevas:
pyproject.toml el mas importante y algo nuevo. Define tu sistema de build, el metadata del proyecto, y configuraciones para las herramientas como Black (formater) o Ruff (linter)

carpeta de src: Ayuda para que no solo funcione en tu maquina.

### README (con ayuda de Gemini. Obtenido el 15 de mayo de 2025, actualizado el 12 de marzo 2026)
Que hace tu proyecto? - Como instalarlo - Como correrlo

Esta es una API sencilla construida en Python diseñada específicamente para que estudiantes practiquen peticiones HTTP, manejo de JSON y lógica de filtrado de datos.

📌 Descripción
Este proyecto simula un servicio meteorológico. Proporciona datos en tiempo real (simulados) sobre temperatura, humedad y condiciones climáticas de varias ciudades del mundo. Es ideal para aprender a conectar un frontend con un backend.

🚀 Instalación y Configuración
Sigue estos pasos para tener el proyecto funcionando en tu computadora:

Clonar el repositorio:

Bash
git clone https://github.com/CS1400-Biblioteca/mago_meteorologico_m12.git
cd clima-estudiantil
Crear un entorno virtual:

Bash
python -m venv .env
# En Windows:
.env\Scripts\activate
# En Mac/Linux:
source .env/bin/activate
Instalar dependencias:

Bash
pip install -r requisitos.txt
🛠️ Cómo Usar la API
Para iniciar el servidor local, ejecuta:

Bash
python src/asistente_clima/principal.py

Ejercicios Sugeridos
Si estás usando este repo para practicar, intenta completar estos retos:

Filtro de Temperatura: Modifica el archivo motor.py para que solo devuelva ciudades con más de 25°C.

Manejo de Errores: Haz que la API devuelva un mensaje de "Ciudad no encontrada" con un código de error 404 real.

Nueva Funcionalidad: Agrega el campo viento al objeto JSON de respuesta.