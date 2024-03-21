/cars/filter_and_order/?category_id={id}&order_by={field}&order_direction={order}
/cars/filter_and_order/?order_by={field}&order_direction={order}
/cars/filter_and_order/?category_id={nro}

# EGO CHALLENGE API

Catálogo de automoviles para la empresa EGO (api con Django Rest Framework)

## Requisitos Previos

Asegurarse de tener instalado lo siguiente en el sistema:

- Python (versión 3)

## Configuración del Entorno Virtual

Para evitar conflictos con otras aplicaciones Python en tu sistema, puedes usar un entorno virtual. Aquí tienes cómo hacerlo:

1. Instala `virtualenv` si aún no lo has hecho:
    ```bash
    pip install virtualenv
    ```

2. Crea un nuevo entorno virtual en el directorio del proyecto:
    ```bash
    python3 -m venv venv
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```

## Instalación de Dependencias

Instala las dependencias del proyecto usando `pip` (instalar pip en caso de ser necesario):

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

En el archivo settings.py del proyecto, modificar el apartado DATABASES:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Luego correr las migraciónes para la creación de las tablas dentro de la base de datos:

```bash
python manage.py makemigrations

python manage.py migrate
```

## Ejecución del sistema

Una vez realizadas todas las configuraciones necesarias, ejecutar el software de forma local:

```bash
python manage.py runserver
```

Ahora el sistema debería ser accesible desde localhost o 127.0.0.1, utilizando el puerto que se le haya asignado (generalmente es el puerto 8000)

```bash
localhost:8000

127.0.0.1:8000
```
