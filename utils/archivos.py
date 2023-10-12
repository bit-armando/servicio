import boto3
import streamlit as st
import pandas as pd
from io import StringIO

@st.cache_data
def get_df_s3(nombre_archivo, _s3_client):
    response = _s3_client.get_object(
        Bucket='servicio-uacj',
        Key=nombre_archivo
    )
    contenido = response['Body'].read().decode('latin-1')
    df = pd.read_csv(StringIO(contenido))
    return df        