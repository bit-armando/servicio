import streamlit as st
import os

st.markdown("# Dir 📁")
st.sidebar.markdown("# Dir 📁")


carpeta_data = './data'
nombres_archivos = os.listdir(carpeta_data)

for nombre_archivo in nombres_archivos:
  agree = st.checkbox(nombre_archivo)


if agree:
  st.write('Great!')