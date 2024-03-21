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
    python -m venv venv
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

Instala las dependencias del proyecto usando `pip`:

```bash
pip install -r requirements.txt
