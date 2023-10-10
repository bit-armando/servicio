import streamlit as st
import boto3
import pandas as pd
from io import StringIO

st.markdown("# Dir 📁")
st.sidebar.markdown("# Dir 📁")

# Listar los nombres de los archivos del bucket
s3 = boto3.resource('s3')
buket = s3.Bucket('servicio-uacj')
nombres_archivos = []
for obj in buket.objects.all():
    nombres_archivos.append(obj.key)


archivos_seleccionados = []
for nombre_archivo in nombres_archivos:
    seleccionado = st.checkbox(nombre_archivo)
    if seleccionado:
        archivos_seleccionados.append(nombre_archivo)


if st.button("Combinar", type="primary"):
    i = len(archivos_seleccionados)
    if i == 0 or i == 1:
        st.write("Agrega mas de un archivo para combinar")
    else:
        dataframes = []
        s3_client = boto3.client('s3')
        for file in archivos_seleccionados:
            response = s3_client.get_object(
                Bucket='servicio-uacj',
                Key=file
            )
            contenido = response['Body'].read().decode('latin-1')
            df = pd.read_csv(StringIO(contenido))
            dataframes.append(df)

        resultado = pd.concat(dataframes, ignore_index=True)

        st.download_button(
            label="Descargar",
            data=resultado.to_csv(index=False, encoding='latin-1'),
            file_name='resultado.csv',
            mime='text/csv'
        )

        st.write('DataFrames combinados')