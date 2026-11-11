
import pandas as pd
import numpy as np

silver = pd.read_parquet("transacoes_silver.parquet")
gold = pd.read_parquet("resumo_fraude_gold.parquet")


gold_esperada = (
    silver.groupby(["canal", "tipo_transacao"])
    .agg(
        total_transacoes=("id_transacao", "count"),
        total_valor=("valor", "sum"),
        ticket_medio=("valor", "mean"),
        volume_suspeito_fraude=(
            "flag_suspeita_fraude", "sum"
        )
    )
    .reset_index()
)

chaves = ["canal", "tipo_transacao"]

gold = gold.sort_values(chaves).reset_index(drop=True)
gold_esperada = gold_esperada.sort_values(chaves).reset_index(drop=True)

# Compara as colunas
print("Quantidade de grupos:", len(gold))
print("Grupos esperados:", len(gold_esperada))

print(
    "Contagens corretas:",
    gold["total_transacoes"].equals(
        gold_esperada["total_transacoes"]
    )
)

print(
    "Valores totais corretos:",
    np.allclose(
        gold["total_valor"],
        gold_esperada["total_valor"],
        rtol=1e-9,
        atol=1e-6
    )
)

print(
    "Tickets médios corretos:",
    np.allclose(
        gold["ticket_medio"],
        gold_esperada["ticket_medio"],
        rtol=1e-9,
        atol=1e-6
    )
)

print(
    "Suspeitas corretas:",
    gold["volume_suspeito_fraude"].equals(
        gold_esperada["volume_suspeito_fraude"]
    )
)
