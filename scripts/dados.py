import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path

np.random.seed(42)
random.seed(42)

num_records = 10000

transacao_ids = [f"TXN-{100000 + i}" for i in range(num_records)]
cliente_ids = [f"CLI-{random.randint(1000, 2500)}" for _ in range(num_records)]
tipos_transacao = np.random.choice(['PIX', 'CARTAO_CREDITO', 'CARTAO_DEBITO', 'TED'], size=num_records, p=[0.5, 0.3, 0.15, 0.05])
valores = np.round(np.random.exponential(scale=150, size=num_records) + 5, 2)


for i in range(0, num_records, 150):
    valores[i] = round(random.uniform(5000, 25000), 2)

start_date = datetime(2026, 1, 1)
timestamps = [start_date + timedelta(minutes=random.randint(0, 100000)) for _ in range(num_records)]
canais = np.random.choice(['APP_MOBILE', 'INTERNET_BANKING', 'MAQUININHA', 'CAIXA_ELETRONICO'], size=num_records, p=[0.6, 0.25, 0.1, 0.05])
status_transacao = np.random.choice(['APROVADA', 'NEGADA', 'EM_ANALISE'], size=num_records, p=[0.92, 0.05, 0.03])
flag_suspeita_fraude = [1 if (val > 8000 or status == 'EM_ANALISE') else 0 for val, status in zip(valores, status_transacao)]

df = pd.DataFrame({
    'id_transacao': transacao_ids,
    'id_cliente': cliente_ids,
    'tipo_transacao': tipos_transacao,
    'valor': valores,
    'data_hora': timestamps,
    'canal': canais,
    'status': status_transacao,
    'flag_suspeita_fraude': flag_suspeita_fraude
})


caminho_saida = Path(__file__).resolve().parent.parent / "dados" / "bronze" / "transacoes_bancarias_raw.csv"
caminho_saida.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(caminho_saida, index=False)
print("Dataset 'transacoes_bancarias_raw.csv' gerado com sucesso!")