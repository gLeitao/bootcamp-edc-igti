import boto3
import pandas as pd


#criar um cliente para interagir com aws s3

s3_cliente = boto3.client('s3')

s3_cliente.download_file('datalake-geovani-igti', 'data/Municipios_SC.csv', 'data/Municipios_SC.csv')

df = pd.read_csv('data/Municipios_SC.csv', sep=';')

print(df.head())

s3_cliente.upload_file('data/Separatrizes.csv', 'datalake-geovani-igti', 'data/Separatrizjob.csv')