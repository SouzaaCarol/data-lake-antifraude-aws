
CREATE EXTERNAL TABLE IF NOT EXISTS default.tbl_resumo_fraude_gold (
    canal STRING,
    tipo_transacao STRING,
    total_transacoes BIGINT,
    total_valor DOUBLE,
    ticket_medio DOUBLE,
    volume_suspeito_fraude BIGINT
)
STORED AS PARQUET
LOCATION 's3://seu-bucket-exemplo/gold/';
