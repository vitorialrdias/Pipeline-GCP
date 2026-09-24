CREATE TABLE IF NOT EXISTS `project-cb4de469-9a26-4595-bfd.trusted_imoveis_sp.imoveis`
(
  imovel_id        STRING      NOT NULL,
  price             FLOAT64,
  condo_price       FLOAT64,
  size_m2           INT64,
  rooms             INT64,
  toilets           INT64,
  suites            INT64,
  parking_spots     INT64,
  has_elevator      BOOL,
  is_furnished      BOOL,
  has_swimming_pool BOOL,
  is_new            BOOL,
  district          STRING,
  negotiation_type  STRING,
  property_type     STRING,
  latitude          FLOAT64,
  longitude         FLOAT64,
  price_per_m2      FLOAT64,
  ingestion_date     DATE
)
PARTITION BY ingestion_date
CLUSTER BY district;