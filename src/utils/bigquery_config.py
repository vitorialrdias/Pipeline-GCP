import os
from google.cloud import bigquery

PROJECT_ID = os.environ.get("vitorialrdias", "project-cb4de469-9a26-4595-bfd")
LOCATION = os.environ.get("southamerica-east4", "US")

DATASET_RAW = "raw_imoveis_sp"
DATASET_TRUSTED = "trusted_imoveis_sp"
DATASET_ANALYTICS = "analytics_imoveis_sp"
TABLE_STAGING_IMOVEIS = f"{PROJECT_ID}.{DATASET_RAW}.stg_imoveis"
TABLE_TRUSTED_IMOVEIS = f"{PROJECT_ID}.{DATASET_TRUSTED}.imoveis"

def get_bigquery_client() -> bigquery.Client:
    return bigquery.Client(project=PROJECT_ID, location=LOCATION)
