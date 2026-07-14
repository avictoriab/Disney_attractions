import streamlit as st
import pandas as pd
from database import SessionLocal
import models
import scraper

# Título de la app
st.title("Estado de Atracciones: Magic Kingdom")

# Actualización automática
with st.spinner('Conectando y actualizando tiempos...'):
    try:
        scraper.ejecutar_scraping()
        st.success('¡Datos actualizados!')
    except Exception as e:
        st.error(f'Error al actualizar: {e}')

# Botón para refrescar datos
if st.button("Actualizar datos"):
    st.rerun()

#Contenedor vacío para mostrar la tabla
placeholder = st.empty()

# Mostrar el mensaje de "cargando" mientras se lee la base de datos
with placeholder.container():
    with st.spinner('Cargando datos desde la base de datos...'):
        # Leer la base de datos
        db = SessionLocal()
        atracciones = db.query(models.Atraccion).all()
        db.close()
        
        # Convertir los datos a DataFrame
        data = [{"Nombre": a.nombre, "Tiempo": a.tiempo_espera} for a in atracciones]
        df = pd.DataFrame(data)

# Reemplazar el contenedor de carga con la tabla final
with placeholder.container():
    # Mostrar la tabla
    st.table(df)



# Filtrar la tabla

st.subheader("Buscador de atracciones")
busqueda = st.text_input("Escribe el nombre de la atracción...")
if busqueda:
    df_filtrado = df[df["Nombre"].str.contains(busqueda, case=False)]
    st.write(df_filtrado)