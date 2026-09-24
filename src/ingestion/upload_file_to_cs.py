import sys
import logging
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
    
logger = logging.getLogger(__name__)

BUCKET_RAW = "raw_files_imoveis"
def upload_file_storage(local_path: str) -> str:
    try:
        execution_date = date.today()
        destination_storage = f"imoveis_sp/dt={execution_date.isoformat()}/imoveis.csv"
        
        client = get_storage_client()
        
        bucket = client.bucket(BUCKET_RAW)
        storage = bucket.blob(destination_storage)
        
        storage.upload_from_filename(local_path)
        logger.info("Arquivo %s enviado para gs://%s/%s", local_path, BUCKET_RAW, destination_storage)
        
        return f"gs://{BUCKET_RAW}/{destination_storage}"
        
    except Exception as e:
        logger.error(e)
        

if __name__ == "__main__":
    from utils.storage_config import get_storage_client
    logging.basicConfig(level=logging.INFO)
    gcs_uri = upload_file_storage(local_path="data/dataset_imoveis_sp.csv")
    print(gcs_uri)