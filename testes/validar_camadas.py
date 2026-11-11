import pandas as pd

raw = pd.read_csv("transacoes_bancarias_raw.csv")
silver = pd.read_parquet("transacoes_silver.parquet")
gold = pd.read_parquet("resumo_fraude_gold.parquet")

print("BRONZE:", raw.shape)
print("SILVER:", silver.shape)
print("GOLD:", gold.shape)

print("\nColunas Silver:")
print(silver.dtypes)

print("\nColunas Gold:")
print(gold.dtypes)

print("\nTotal de transações Bronze:", len(raw))
print("Total de transações Silver:", len(silver))

print(
    "\nTotal de transações Gold:",
    gold["total_transacoes"].sum()
)