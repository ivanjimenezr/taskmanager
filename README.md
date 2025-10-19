# TaskManager

TaskManager es un proyecto minimalista en Python para gestionar tareas (task manager) usado como ejercicio y demostración en el marco del máster de desarrollo en IA. Incluye una pequeña API/servicio local, utilidades para gestionar tareas y pruebas automatizadas.

## Contenido de este README

- Descripción
- Requisitos
- Instalación
- Uso (línea de comandos y API)
- Estructura del proyecto
- Ejecutar tests
- Contribuir
- Licencia y contacto

## Descripción

Este repositorio contiene una implementación sencilla para crear, listar y gestionar tareas. Está pensada como base para prácticas de programación, pruebas unitarias y como ejemplo didáctico para integrar servicios pequeños en proyectos de IA.

## Requisitos

- Python 3.8+ recomendado
- pip
- (Opcional) un entorno virtual (venv, virtualenv, conda)

Las dependencias del proyecto están en `requirements.txt`.

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/ivanjimenezr/taskmanager.git
cd taskmanager
```

2. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:

```bash
python -m pip install -r requirements.txt
```

## Uso

Este proyecto contiene varios archivos principales:

- `main.py`: punto de entrada principal (si aplica)
- `task_manager.py`: lógica principal para manipular tareas
- `ai_service.py`: ejemplo de servicio relacionado con IA (si aplica)
- `tasks.json`: datos de ejemplo/almacenamiento

Ejemplos de uso (línea de comandos):

```bash
# Ejecutar el script principal
python main.py

# Ejecutar el servicio AI (si corresponde)
python ai_service.py
```

Revisa los docstrings en los módulos para ver las funciones públicas y parámetros.

## Estructura del proyecto

Raíz del repositorio:

- `ai_service.py` - Servicio/ejemplo relacionado con IA.
- `main.py` - Punto de entrada para demostraciones.
- `task_manager.py` - Lógica de creación, lectura, actualización y borrado de tareas.
- `tasks.json` - Datos de ejemplo persistidos en versión simple JSON.
- `test_task_manager_root.py` - Tests unitarios con pytest.
- `requirements.txt` - Dependencias del proyecto.
- `README.md` - Este archivo.

## Ejecutar tests

Este proyecto usa `pytest`. Para ejecutar los tests:

```bash
pytest -q
```

Si no tienes pytest instalado, instálalo:

```bash
python -m pip install pytest
```

Nota: Cambiar el README no debería afectar la ejecución de tests, pero es buena práctica ejecutar la suite para confirmar que todo sigue pasando.

## Contribuir

Contribuciones pequeñas y claras son bienvenidas.

1. Haz un fork del repositorio.
2. Crea una rama con un nombre descriptivo.
3. Abre un Pull Request con una descripción clara del cambio.

Por favor añade tests cuando el cambio afecte la lógica.

## Licencia

Incluye aquí la licencia del proyecto (por ejemplo, MIT). Si no hay licencia específica, añade la que corresponda o consulta al propietario.

## Contacto

Para preguntas o sugerencias, abre un issue en el repositorio o contacta a los mantenedores.

---

Si quieres, puedo:

- Añadir badges (build, coverage) al README.
- Escribir ejemplos más detallados de la API o fragmentos de código de uso.
- Crear un archivo `CONTRIBUTING.md` y plantillas de PR/issue.

Dime qué prefieres y lo implemento.
hola
