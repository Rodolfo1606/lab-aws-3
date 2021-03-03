import boto3
import pandas as pd
from boto3.s3.transfer import S3Transfer

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAZFTRYRXCABHDZVNV',
    aws_secret_access_key = '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',
    region_name = 'us-east-1'
)


# extraer archivo desde el bucket
obj = client.get_object(
    Bucket='taxi-data-eedf2cb2-3030-43f2-bd83-a3693ba71b05',
    Key='train_Rodolfo_comando.csv'
)

# leer la data del archivo
data = pd.read_csv(obj['Body'])

# Edicion de  la data en el terminal

del(data['vendor_id'])
del(data['trip_duration'])
data = data.fillna(0)


# Guardar en csv
data.to_csv('train_edited_rodolfo.csv')

#Subir archivo

S3Transfer(client).upload_file('train_edited_rodolfo.csv', 'taxi-data-eedf2cb2-3030-43f2-bd83-a3693ba71b05' ,
                     'train_edited_rodolfo.csv',)


