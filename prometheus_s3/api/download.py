from .download_helper import *
from datetime import datetime

def is_date_in_range(date, start_date, end_date) -> bool:
   '''Check wheather date is in range start_date and end_date'''
   print(start_date, date, end_date)
   return start_date <= date <= end_date

def get_date_object(string):
    '''Converts the date_string into date object'''
    s = string.split('/')[1][:16]
    return datetime.strptime(s, "%Y%m%dT%H%M%SZ")

def download(path, date_string):
    # print(path, date_string)
    date_object = datetime.strptime(date_string, "%d-%m-%Y")

    bucket_name = 'my-local-bucket'
    local_folder = 'downloaded_folder' 
    folder_list = getFolders(bucket_name, path+'/')

    print(folder_list)
    # folder_list = folder_list.strip('/')[1]
    for i in range(len(folder_list)-1):
        start_date, end_date = get_date_object(folder_list[i]), get_date_object(folder_list[i+1])
        # print(start_date, end_date)
        if is_date_in_range(date_object, start_date, end_date):
            download_folder_from_s3(bucket_name,f'{path}/{end_date.strftime("%Y%m%dT%H%M%SZ")}', local_folder)
            break
        # print(end_date.strftime("%Y%m%dT%H%M%SZ"), 'found')

# download_folder_from_s3(bucket_name, s3_folder, local_folder)
