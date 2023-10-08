import streamlit as st
import pandas as pd

st.markdown("# Drag and Drop 🗒️")
st.sidebar.markdown("# Drag and Drop 🗒️")    

uploaded_files = st.file_uploader(
    "Suelta los archivos .CSV", accept_multiple_files=True)

if st.button("Combinar", type="primary"):
    i = len(uploaded_files)
    if i == 0 or i == 1:
        st.write("Agrega mas de un archivo para combinar")
    else:
        dataframes = []
        for file in uploaded_files:
            df = pd.read_csv(file, encoding='utf-8')
            dataframes.append(df)

        resultado = pd.concat(dataframes, ignore_index=True)
        # resultado.to_csv('resultado.csv', index=False, encoding='utf-8')

        st.download_button(
            label="Descargar",
            data=resultado.to_csv(index=False, encoding='utf-8'),
            file_name='resultado.csv',
            mime='text/csv'
        )

        st.write('DataFrames combinados')
