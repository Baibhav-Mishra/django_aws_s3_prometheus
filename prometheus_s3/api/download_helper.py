import boto3
from botocore.client import Config
import os
import cred
from multiprocessing import Pool
from functools import partial

s3 = boto3.client(
    's3',
    endpoint_url= cred.endpoint_url,
    aws_access_key_id=cred.aws_access_key_id,
    aws_secret_access_key=cred.aws_secret_access_key,
    region_name=cred.region_name,
)
def download_files_in_parallel(response):
    partial_worker = partial(download_folder_from_s3, re)
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(download_folder_from_s3, response)


def download_folder_from_s3(bucket_name: str, s3_folder: str, local_folder: str):

    # Ensure the local folder exists
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
    
    # List objects in the specified S3 folder
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)
    # print(response)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_key = obj['Key']
            local_file_path = os.path.join(local_folder, s3_key)
            print(local_file_path)
            
            # Ensure the local directory exists
            local_file_dir = os.path.dirname(local_file_path)
            if not os.path.exists(local_file_dir):
                os.makedirs(local_file_dir)
            
            s3.download_file(bucket_name, s3_key, local_file_path)
            print(f"Downloaded {s3_key} to {local_file_path}")

# Download the folder from S3
def getFolders(bucket_name: str, prefix: str) -> list:
    '''Returns a list of all the folder containing the common prefix '''
    folder_list = []
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix,Delimiter='/')
    for obj in response.get('CommonPrefixes'):
        folder_list.append(obj.get('Prefix'))
    return folder_list