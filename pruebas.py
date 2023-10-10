import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

response = s3.get_object(
    Bucket='servicio-uacj',
    Key='desayunos_klimon.csv'
)

contenido = response['Body'].read().decode('latin-1')

df = pd.read_csv(StringIO(contenido))

nombre1 = df['nombre']
print(nombre1[1])