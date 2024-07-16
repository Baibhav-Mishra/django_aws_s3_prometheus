import boto3
from botocore.client import Config
import os
from multiprocessing.pool import ThreadPool 
# Configure boto3 to use LocalStack
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1',
)

# directory = '/home/baibhav/Documents/local_stack/snapshots'
bucket_name = 'my-local-bucket'
# s3.create_bucket(Bucket=bucket_name)

def upload_directory(name, s3_directory):
    full_local_directory_path = f'/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/snapshots/{name}'
    for root, dirs, files in os.walk(full_local_directory_path):
        for filename in files:
            # Construct the full local path
            local_path = os.path.join(root, filename)

            # Construct the relative path and S3 path
            relative_path = os.path.relpath(local_path, full_local_directory_path)
            s3_path = os.path.join(s3_directory, relative_path).replace("\\", "/")

                # Upload the file
            try:
                s3.upload_file(local_path, bucket_name, s3_path)
                print(f'Successfully uploaded {local_path} to {s3_path}')
            except FileNotFoundError:
                print(f'The file was not found: {local_path}')
# pool = ThreadPool(processes=10)
# pool.map(upload_directory, filenames)
# Upload the directory
# print("fuck")
# upload_directory("/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/snapshots/20240712T071112Z-27ac82967eee3e46", "localhost:9091/20240712T071112Z")
# for (root,dirs,files) in os.walk('/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/snapshots/20240712T071112Z-27ac82967eee3e46', topdown=True):
#         # print (root)
#         print (dirs)
        # print (files)