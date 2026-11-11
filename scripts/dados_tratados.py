import pandas as pd
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent.parent


caminho_bronze = pasta_projeto / "dados" / "bronze" / "transacoes_bancarias_raw.csv"
df_raw = pd.read_csv(caminho_bronze)


df_silver = df_raw.copy()
df_silver['data_hora'] = pd.to_datetime(df_silver['data_hora'])
df_silver['ano_mes'] = df_silver['data_hora'].dt.to_period('M').astype(str)

caminho_silver = pasta_projeto / "dados" / "prata" / "transacoes_silver.parquet"
caminho_silver.parent.mkdir(parents=True, exist_ok=True)

df_silver.to_parquet(caminho_silver, index=False)


df_gold_fraude = df_silver.groupby(['canal', 'tipo_transacao']).agg(
    total_transacoes=('id_transacao', 'count'),
    total_valor=('valor', 'sum'),
    ticket_medio=('valor', 'mean'),
    volume_suspeito_fraude=('flag_suspeita_fraude', 'sum')
).reset_index()

caminho_gold = pasta_projeto / "dados" / "ouro" / "resumo_fraude_gold.parquet"
caminho_gold.parent.mkdir(parents=True, exist_ok=True)

df_gold_fraude.to_parquet(caminho_gold, index=False)

print("Camadas Prata e Ouro convertidas para Parquet com sucesso!")