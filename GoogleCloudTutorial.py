import os
from google.cloud import storage

# connects to api 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\Kevin Jiang\Documents\GitHub\GoogleCloud\Service_Key.json"

storage_client = storage.Client()
# -------------------------------------

# create a new bucket
bucket_name = 'your_bucket_name'
bucket = storage_client.bucket(bucket_name)
bucket.create = 'US'
bucket = storage_client.create_bucket(bucket)
# -----------------------------------------

# print bucket details
vars(bucket)
# ----------------------

# accessing a specific bucket
my_bucket = storage_client.get_bucket('your_bucket_name')
# ------------------------

# upload files
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r"filepath of folder"
upload_to_bucket('name of upload', os.path.join(file_path, r'file path of data'), 'your_bucket_name')


# download files
def download_file(blob_name, file_path, bucket_name):
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            with open(file_path, 'wb') as f:
                storage_client.download_blob_to_file(blob, f)
            return True
        except Exception as e:
            print(e)
            return False

bucket_name = 'your_bucket_name'
download_file('name of upload', os.path.join(os.getcwd(), 'file1.csv'), bucket_name)