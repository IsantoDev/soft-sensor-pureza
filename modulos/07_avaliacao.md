# Módulo 07 — Avaliação e diagnóstico

## Objetivo
Ir além das métricas numéricas: **visualizar** o comportamento do modelo, analisar
resíduos e identificar onde ele erra sistematicamente.

## Teoria

Métricas sozinhas mentem. Um R² de 0.95 pode esconder um modelo que erra sempre nos
piores momentos (exatamente quando você mais precisa).

**Métricas de regressão:**
- **MAE (Mean Absolute Error):** erro médio em unidade do alvo. Fácil de explicar:
  "o modelo erra em média X pontos de pureza".
- **RMSE (Root Mean Squared Error):** penaliza erros grandes mais que o MAE. Bom para
  detectar falhas pontuais graves.
- **R²:** fração da variância explicada pelo modelo. R²=1 é perfeito; R²=0 é igual à
  média; **R² negativo** significa que o modelo é pior que simplesmente prever a média
  — sinal de problema grave.

**Análise de resíduos** (resíduo = real − previsto):
- Resíduos aleatórios em torno de zero → modelo bem calibrado.
- Padrão sistemático nos resíduos → o modelo não capturou alguma estrutura nos dados
  (ex: erro cresce com o tempo → fouling não modelado).

**Gráficos essenciais:**
- Previsto × Real no tempo (o modelo acompanha a série?).
- Distribuição dos resíduos (histograma ou QQ-plot).
- Resíduo × tempo (há padrão temporal?).

## Prática / Exercícios

Em `meu_trabalho/07_avaliacao.py`, **escreva você**:

1. Plote **previsto × real** no período de teste para o melhor modelo.
2. Calcule os resíduos e plote **resíduo × tempo**. Há algum padrão?
3. Plote o histograma dos resíduos. A distribuição é aproximadamente normal?
4. (Diagnóstico) Se os resíduos crescem ao final do período de teste, o que isso
   sugere sobre o modelo e a incrustação?

## Perguntas de fixação
1. O que significa **R² negativo** e o que você faria se visse isso?
2. Se o resíduo tem um padrão em dente-de-serra, o que isso indica?
3. Por que o RMSE penaliza mais erros grandes do que o MAE?

## Checkpoint
Você tem gráficos de diagnóstico e consegue narrar a "história" do que o modelo acerta
e erra. Avance para o **Módulo 08**.
