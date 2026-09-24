import sys
import logging
from google.cloud import bigquery
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
    
logger = logging.getLogger(__name__)

SCHEMA = [
    bigquery.SchemaField("Price", "FLOAT"),
    bigquery.SchemaField("Condo", "FLOAT"),
    bigquery.SchemaField("Size", "INTEGER"),
    bigquery.SchemaField("Rooms", "INTEGER"),
    bigquery.SchemaField("Toilets", "INTEGER"),
    bigquery.SchemaField("Suites", "INTEGER"),
    bigquery.SchemaField("Parking", "INTEGER"),
    bigquery.SchemaField("Elevator", "INTEGER"),
    bigquery.SchemaField("Furnished", "INTEGER"),
    bigquery.SchemaField("Swimming_Pool", "INTEGER"),
    bigquery.SchemaField("New", "INTEGER"),
    bigquery.SchemaField("District", "STRING"),
    bigquery.SchemaField("Negotiation_Type", "STRING"),
    bigquery.SchemaField("Property_Type", "STRING"),
    bigquery.SchemaField("Latitude", "FLOAT"),
    bigquery.SchemaField("Longitude", "FLOAT"),
]

def load_raw_to_staging(gcs_uri: str) -> int:
    try:
        client = get_bigquery_client()
        
        job_config = bigquery.LoadJobConfig(
            schema=SCHEMA,
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        
        laod_job = client.load_table_from_uri(
            gcs_uri, TABLE_STAGING_IMOVEIS, job_config=job_config
        )
        laod_job.result() # espera o job terminar de subir os dados
        
        destination = client.get_table(TABLE_STAGING_IMOVEIS)
        logger.info("Carregadas %s linhas em %s", destination.num_rows, TABLE_STAGING_IMOVEIS)
        return destination.num_rows
    
    except Exception as e:
        logger.error(e)
        

if __name__ == "__main__":
    from utils.bigquery_config import get_bigquery_client, TABLE_STAGING_IMOVEIS
    logging.basicConfig(level=logging.INFO)
    load_raw_to_staging(gcs_uri="gs://raw_files_imoveis/imoveis_sp/dt=2026-09-09/imoveis.csv")
    