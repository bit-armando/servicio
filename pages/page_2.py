import streamlit as st
import os
import pandas as pd

st.markdown("# Dir 📁")
st.sidebar.markdown("# Dir 📁")


carpeta_data = './data'
nombres_archivos = os.listdir(carpeta_data)

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
        for file in archivos_seleccionados:
            df = pd.read_csv('./data/'+file, encoding='utf-8')
            dataframes.append(df)

        resultado = pd.concat(dataframes, ignore_index=True)

        st.download_button(
            label="Descargar",
            data=resultado.to_csv(index=False, encoding='utf-8'),
            file_name='resultado.csv',
            mime='text/csv'
        )

        st.write('DataFrames combinados')