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

X = df.drop(columns=["pureza_produto"])
y = df["pureza_produto"]
df = df.dropna()
n = len(df)
i_treino = int(n * 0.70)
i_val = int(n * 0.85)

X_tr, y_tr = X.iloc[:i_treino], y.iloc[:i_treino]
X_vl, y_vl = X.iloc[i_treino:i_val], y.iloc[i_treino:i_val]
X_te, y_te = X.iloc[i_val:], y.iloc[i_val:]

print(f"Treino: {len(X_tr)} linhas | {X_tr.index.min().date()} a {X_tr.index.max().date()}")
print(f"Valid.: {len(X_vl)} linhas | {X_vl.index.min().date()} a {X_vl.index.max().date()}")
print(f"Teste : {len(X_te)} linhas | {X_te.index.min().date()} a {X_te.index.max().date()}")