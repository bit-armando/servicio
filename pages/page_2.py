import streamlit as st
import boto3
import pandas as pd
# from io import StringIO
from utils.archivos import get_df_s3

st.title("Dir 📁")
st.sidebar.markdown("# Dir 📁")

# Listar los nombres de los archivos del bucket
s3 = boto3.resource('s3')
buket = s3.Bucket('servicio-uacj')
nombres_archivos = []
for obj in buket.objects.all():
    nombres_archivos.append(obj.key)

# Seleccionar los archivos a combinar
archivos_seleccionados = st.multiselect(
    "Selecciona los archivos a combinar",
    nombres_archivos,
    []
)

col1, col2 = st.columns(2)
# selecciona las columndas de un dataframe con un st.checkbos y las guarda en un diccionario
columns_filtradas = []
archivo_filtrado = {}
s3_client = boto3.client('s3')

for nombre_archivo in archivos_seleccionados:
    with col1.expander(nombre_archivo):
        df = get_df_s3(nombre_archivo, s3_client)
        columns = df.columns
        columns_filtradas = st.multiselect(
            "Seleccion de columnas",
            columns,
            [],
            key=nombre_archivo
        )
        archivo_filtrado[nombre_archivo] = columns_filtradas
    
dataframes = []
if st.button("Combinar", type="primary"):
    i = len(archivos_seleccionados)
    if i == 0 or i == 1:
        st.warning('Agrega mas de un archivo para combinarlos', icon="⚠️")
    else:
        for nombre_archivo in archivos_seleccionados:
            df = get_df_s3(nombre_archivo, s3_client)
            df = df[archivo_filtrado[nombre_archivo]]
            df['archivo'] = nombre_archivo
            dataframes.append(df)

        resultado = pd.concat(dataframes, ignore_index=True)
        st.dataframe(resultado.head(5))

        st.download_button(
            label="Descargar",
            data=resultado.to_csv(index=False, encoding='latin-1'),
            file_name='resultado.csv',
            mime='text/csv'
        )

        st.write('DataFrames combinados')
col2.write(archivo_filtrado)