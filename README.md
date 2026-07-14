# Disney Magic Kingdom Wait Times

Esta es una aplicación interactiva desarrollada con Streamlit que permite visualizar los tiempos de espera de las atracciones de Magic Kingdom en tiempo real, utilizando un scraper propio y una base de datos local.

## Características

- **Actualización automática:** Obtención de datos en tiempo real al iniciar la aplicación.
- **Visualización rápida:** Interfaz limpia que muestra los tiempos de espera mediante tablas.
- **Base de datos local:** Almacenamiento eficiente de la información para consultas rápidas.

## Requisitos previos

- Python 3.x instalado.
- Git instalado.

## Instalación y Ejecución

1. **Clona el repositorio:**

   ```bash
   git clone [https://github.com/avictoriab/Disney_attractions.git](https://github.com/avictoriab/Disney_attractions.git)
   cd NOMBRE_DEL_REPOSITORIO

   ```

2. Crea y activa un entorno virtual:

Bash

# En Windows:

python -m venv venv
venv\Scripts\activate

# En Mac/Linux:

python -m venv venv
source venv/bin/activate

3. Instala las dependencias:

Bash
pip install -r requirements.txt

4. Ejecuta la aplicación:

Bash
streamlit run app_visual.py

Estructura del Proyecto

app_visual.py: Interfaz principal construida con Streamlit.

scraper.py: Script encargado de extraer los datos.

models.py: Definición de la estructura de la base de datos.

database.py: Configuración de la conexión a la base de datos.
