CREATE EXTERNAL TABLE IF NOT EXISTS default.tbl_transacoes_silver (
  id_transacao STRING,
  id_cliente STRING,
  tipo_transacao STRING,
  valor DOUBLE,
  data_hora TIMESTAMP,
  canal STRING,
  status STRING,
  flag_suspeita_fraude INT,
  ano_mes STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS PARQUET
LOCATION 's3://seu-bucket-exemplo/silver/';