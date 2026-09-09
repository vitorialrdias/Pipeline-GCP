from google.cloud import storage
from utils.bigquery_config import PROJECT_ID

def get_storage_client() -> storage.Client:
    return storage.Client(project=PROJECT_ID)