"""
01_gerar_dados.py
=================
Gera um dataset SINTÉTICO porém fisicamente plausível de uma coluna de
destilação industrial, para o problema de SOFT SENSOR.

Contexto do problema (o que você conta na entrevista):
- Em uma coluna de destilação, a PUREZA do produto é a variável mais
  importante, mas medi-la exige análise de laboratório: é cara e lenta.
- Em contrapartida, sensores de TEMPERATURA, PRESSÃO e VAZÃO são baratos
  e medidos o tempo todo.
- Um "soft sensor" é um MODELO que estima a pureza a partir desses sensores
  baratos, em tempo real. É exatamente o que a vaga cita.

O dataset tem propriedades de SÉRIE TEMPORAL de propósito:
- tendência   -> incrustação (fouling) degrada a separação ao longo do tempo
- sazonalidade-> ciclo diário de temperatura ambiente
- defasagem   -> o estado atual depende do estado das horas anteriores
- faltantes   -> sensores "caem" (dropout) como na vida real
Essas quatro coisas são literalmente os requisitos de séries temporais da vaga.
"""

import numpy as np
import pandas as pd

# Semente fixa -> resultado reproduzível. Em entrevista isso mostra rigor.
rng = np.random.default_rng(42)

# ----------------------------------------------------------------------
# 1) Eixo de tempo: 120 dias de leituras HORÁRIAS
# ----------------------------------------------------------------------
n = 24 * 120                                   # 2880 pontos
idx = pd.date_range("2025-09-01", periods=n, freq="h")
t = np.arange(n)                               # contador inteiro 0..n-1

# Ciclo diário (-1 a 1): temperatura ambiente sobe de dia, cai de noite
ciclo_diario = np.sin(2 * np.pi * idx.hour / 24)

# Horas desde a última manutenção: a coluna é LIMPA a cada 30 dias (720h).
# A incrustação cresce e RESETA na limpeza -> padrão recorrente (dente-de-serra),
# bem mais realista que uma queda infinita. É uma variável que o operador conhece.
horas_desde_manutencao = t % 720

# ----------------------------------------------------------------------
# 2) Variáveis de operação (entradas do processo)
# ----------------------------------------------------------------------
# Vazão de alimentação: oscila com um ciclo semanal + ruído
vazao_alimentacao = 100 + 8 * np.sin(2 * np.pi * t / (24 * 7)) + rng.normal(0, 3, n)
vazao_alimentacao = np.clip(vazao_alimentacao, 80, 130)

# Vazão de refluxo: controlada num setpoint. NA METADE do período o operador
# AUMENTA o refluxo para compensar a perda de separação (história realista).
setpoint_refluxo = np.where(t > n * 0.5, 75.0, 70.0)
vazao_refluxo = setpoint_refluxo + rng.normal(0, 2, n)

# Razão de refluxo: variável-chave de separação (refluxo / alimentação)
razao_refluxo = vazao_refluxo / vazao_alimentacao

# Pressão e temperatura da alimentação (sensores baratos)
pressao = 1.20 + 0.05 * ciclo_diario + rng.normal(0, 0.02, n)
temp_alimentacao = 85 + 4 * ciclo_diario + rng.normal(0, 1.0, n)

# ----------------------------------------------------------------------
# 3) Sensores de temperatura da coluna (correlacionados com a operação)
# ----------------------------------------------------------------------
# Mais refluxo -> topo MAIS FRIO (melhor separação).
temp_topo = 80 - 8 * (razao_refluxo - 0.70) + 0.5 * ciclo_diario + rng.normal(0, 0.4, n)
# Mais refluxo -> fundo MAIS QUENTE.
temp_fundo = 118 + 6 * (razao_refluxo - 0.70) + rng.normal(0, 0.5, n)

# ----------------------------------------------------------------------
# 4) Variável-ALVO: pureza do produto (%)
# ----------------------------------------------------------------------
# Incrustação (fouling): degrada a separação até ~4 pontos em cada ciclo de
# 30 dias e volta a zero após a limpeza. Recorrente -> o modelo consegue aprender.
fouling = 4.0 * (horas_desde_manutencao / 720)

# tanh -> ganho de pureza com refluxo SATURA (não passa de 100%). Física real.
pureza = (
    94.0
    + 5.0 * np.tanh(3.0 * (razao_refluxo - 0.70))   # refluxo ajuda (saturando)
    - 0.6 * (temp_topo - 78.0)                       # topo quente -> pior
    - fouling                                        # tendência de queda
    + 0.8 * ciclo_diario                             # leve efeito diário
    + rng.normal(0, 0.35, n)                         # ruído de medição
)
pureza = np.clip(pureza, 80.0, 99.9)

# ----------------------------------------------------------------------
# 5) Monta o DataFrame
# ----------------------------------------------------------------------
df = pd.DataFrame({
    "timestamp": idx,
    "temp_topo": temp_topo,
    "temp_fundo": temp_fundo,
    "pressao": pressao,
    "vazao_alimentacao": vazao_alimentacao,
    "vazao_refluxo": vazao_refluxo,
    "temp_alimentacao": temp_alimentacao,
    "horas_desde_manutencao": horas_desde_manutencao,   # variável operacional
    "pureza_produto": pureza,           # <- ALVO
})

# ----------------------------------------------------------------------
# 6) Injeta DADOS FALTANTES (realismo: sensores caem)
# ----------------------------------------------------------------------
sensores = ["temp_topo", "temp_fundo", "pressao",
            "vazao_alimentacao", "vazao_refluxo", "temp_alimentacao"]

# 6a) Dropouts aleatórios: ~3% de cada sensor vira NaN
for col in sensores:
    mask = rng.random(n) < 0.03
    df.loc[mask, col] = np.nan

# 6b) Falha em bloco: sensor de pressão fica 14h offline (manutenção)
df.loc[1000:1013, "pressao"] = np.nan

df.to_csv("dados/sensores_coluna_destilacao.csv", index=False)

print(f"Dataset gerado: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(f"Período: {df['timestamp'].min()} -> {df['timestamp'].max()}")
print("\n% de faltantes por coluna:")
print((df[sensores].isna().mean() * 100).round(2).astype(str) + " %")
print("\nPrimeiras linhas:")
print(df.head().to_string(index=False))
