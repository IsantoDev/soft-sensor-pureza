import pandas as pd

df = pd.read_csv('dados/sensores_coluna_destilacao.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp').sort_index()

SENSORES = ["temp_topo", "temp_fundo", "pressao",
            "vazao_alimentacao", "vazao_refluxo", "temp_alimentacao"]

df[SENSORES] = df[SENSORES].interpolate(method="time").ffill().bfill()

print(df.shape)
for col in SENSORES:
    for lag in [1, 2, 3]:
        df[f"{col}_lag{lag}"] = df[col].shift(lag)

print(df.columns.tolist())      
for col in SENSORES:
    df[f"{col}_med6"] = df[col].rolling(6).mean()
    df[f"{col}_std6"] = df[col].rolling(6).std()

df["hora"] = df.index.hour
df["dia_semana"] = df.index.dayofweek

df = df.dropna()
print(df.shape)