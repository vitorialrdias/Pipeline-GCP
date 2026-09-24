import sys
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))


logger = logging.getLogger(__name__)

def run_staging_to_trusted():
    client = get_bigquery_client()
    query = Path("sql/transform/stg_to_trusted.sql").read_text()

    job = client.query(query)
    job.result()

    logger.info(
        "Transformação staging -> trusted concluída. Bytes processados: %s",
        job.total_bytes_processed,
    )


if __name__ == "__main__":
    from utils.bigquery_config import get_bigquery_client
    logging.basicConfig(level=logging.INFO)
    run_staging_to_trusted()