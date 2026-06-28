import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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

df["hora"] = df.index.hour
df["dia_semana"] = df.index.dayofweek
df = df.dropna() 

X = df.drop(columns=["pureza_produto"])
y = df["pureza_produto"]

n = len(df)
i_treino = int(n * 0.70)
i_val = int(n * 0.85)

X_tr, y_tr = X.iloc[:i_treino], y.iloc[:i_treino]
X_vl, y_vl = X.iloc[i_treino:i_val], y.iloc[i_treino:i_val]
X_te, y_te = X.iloc[i_val:], y.iloc[i_val:]


lab = y.copy()
manter = (np.arange(len(y)) % 8) == 0
lab[~manter] = np.nan
base_pred = lab.ffill().iloc[i_val:]

print('Baseline criado:', len(base_pred), 'previsões')

modelos = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42 ),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=200, random_state=42),
}

resultados = []

for nome, modelo in modelos.items():
    modelo.fit(X_tr, y_tr)
    pred = modelo.predict(X_te)
    mae = mean_absolute_error(y_te, pred)
    rmse = mean_squared_error(y_te, pred)**0.5
    r2 = r2_score(y_te, pred)
    resultados.append({'Modelo': nome, 'MAE': mae, 'RMSE': rmse, 'R2': r2})
    print(f"{nome}: MAE={mae:.4f}, RMSE={rmse:.4f}, R2={r2:.4f}")