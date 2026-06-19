import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados/sensores_coluna_destilacao.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp').sort_index()
SENSORES = ["temp_topo", "temp_fundo", "pressao",
            "vazao_alimentacao", "vazao_refluxo", "temp_alimentacao"]

print("ANTES:")
print(df[SENSORES].isna().sum())

df[SENSORES] = df[SENSORES].interpolate(method="time").ffill().bfill()

print("\nDEPOIS:")
print(df[SENSORES].isna().sum())