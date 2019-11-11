import os

import boto3

access_key_id = os.environ.get('access_key_id')
secret_access_key = os.environ.get('secret_access_key')
bucket_name = os.environ.get('bucket_name')
bucket_location = os.environ.get('bucket_location')

s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
)

def upload_file(filename):
    s3_client.upload_file(filename, bucket_name, filename)
    return f'https://{bucket_name}.{bucket_location}.amazonaws.com/{filename}'

