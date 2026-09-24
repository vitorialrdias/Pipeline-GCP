CREATE OR REPLACE TABLE `project-cb4de469-9a26-4595-bfd.trusted_imoveis_sp.imoveis`
PARTITION BY ingestion_date
CLUSTER BY district AS

SELECT
  TO_HEX(MD5(CONCAT(CAST(Price AS STRING), District, CAST(Size AS STRING), CAST(Latitude AS STRING)))) AS imovel_id,
  Price                                   AS price,
  Condo                                   AS condo_price,
  Size                                    AS size_m2,
  Rooms                                   AS rooms,
  Toilets                                 AS toilets,
  Suites                                  AS suites,
  Parking                                 AS parking_spots,
  Elevator = 1                            AS has_elevator,
  Furnished = 1                           AS is_furnished,
  Swimming_Pool = 1                       AS has_swimming_pool,
  `New` = 1                                 AS is_new,
  INITCAP(TRIM(District))                 AS district,
  UPPER(TRIM(Negotiation_Type))           AS negotiation_type,
  UPPER(TRIM(Property_Type))              AS property_type,
  Latitude                                AS latitude,
  Longitude                               AS longitude,
  SAFE_DIVIDE(Price, NULLIF(Size, 0))     AS price_per_m2,
  CURRENT_DATE()                          AS ingestion_date
FROM `project-cb4de469-9a26-4595-bfd.raw_imoveis_sp.stg_imoveis`
WHERE Price > 0
  AND Size > 0
  AND District IS NOT NULL
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY CAST(Price AS STRING), District, Size, CAST(Latitude AS STRING), CAST(Longitude AS STRING)
  ORDER BY Price
) = 1;