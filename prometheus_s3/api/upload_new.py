import boto3
import os
from multiprocessing import Pool
from functools import partial
from .cred import *
s3_client = boto3.client(
    's3',
    endpoint_url= endpoint_url,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)

bucket_name = bucket

def upload_file(file_path, s3_path, start_dir):
    """
    Function to upload a single file to an S3 bucket
    """
    try:
        # Extract the file name
        file_name = os.path.join(s3_path,os.path.relpath(file_path, start_dir))
        # Upload the file
        print(file_path, file_name)
        s3_client.upload_file(file_path, bucket_name, file_name)
        print(f"Successfully uploaded {file_name}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")


# def upload_files_in_parallel(file_paths, s3_path, start_dir):
#     """
#     Function to upload files to S3 in parallel using multiprocessing
#     """
#     partial_worker = partial(upload_file, s3_path=s3_path, start_dir=start_dir)
#     with Pool(processes=os.cpu_count()) as pool:
#         pool.map(partial_worker, file_paths)


def get_all_files(directory):
    """
    Recursively get all files in the given directory
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def upload(name, s3_path):
    s3_client.create_bucket(Bucket=bucket_name)
    dir = f'/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/snapshots/{name}'
    files_to_upload = get_all_files(dir)
    upload_file(files_to_upload, s3_path, dir)


# upload('20240708T085149Z-27b79b8f04946159','localhost:9090/20240708T085149Z-27b79b8f04946159')