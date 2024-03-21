# EGO CHALLENGE API

Catálogo de automoviles para la empresa EGO (api con Django Rest Framework)

## Requisitos Previos

Asegurarse de tener instalado lo siguiente en el sistema:

- Python (versión 3)

## Clonación del repositorio

El sistema puede ser descargado en forma de archivo comprimido (.zip) o bien puede ser clonado dentro de una carpeta indicada

```bash
git clone https://github.com/JuanHernandezFeser/Car_catalog_EGO_Challenge.git .
```

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

En caso de utilizar una base de datos diferente a la que se provee en el proyecto, correr las migraciónes para la creación de las tablas dentro de la base de datos:

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

## ADMIN

Para acceder al /admin/ de la API, es necesario loguearse con:

Usuario

```bash
superadmin
```
Contraseña

```bash
123456
```

O bien crear un nuevo superusuario utilizando el siguiente comando:

```bash
python3 manage.py createsuperuser
```

## URLS importantes

Para acceder al listado de automoviles realizando un filtro según la categoría en la que se encuentran y ordenandolos por el año o el precio, utilizamos la siguiente ruta:

```bash
/cars/filter_and_order/?category_id={id}&order_by={field}&order_direction={order}
```

Por ejemplo:

```bash
/cars/filter_and_order/?category_id=1&order_by=year&order_direction=asc
```

De la misma forma, se pueden realizar ordenamientos por año/precio, sin haber realizado un filtrado previo:

```bash
/cars/filter_and_order/?order_by={field}&order_direction={order}
```

O bien, se puede realizar un filtrado por categoría, utilizando el ordenamiento por defecto:

```bash
/cars/filter_and_order/?category_id={nro}
```
