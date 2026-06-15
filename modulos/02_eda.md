# Módulo 02 — EDA e qualidade de dados

## Objetivo
Explorar os dados antes de modelar: entender distribuições, relações entre sensores e
o alvo, e **diagnosticar problemas de qualidade** (faltantes, outliers).

## Teoria

**EDA (Exploratory Data Analysis)** é a etapa em que você "conversa" com os dados
antes de qualquer modelo. Pular EDA é a causa nº 1 de modelos que falham em produção.
Você procura responder:

- Como o **alvo** se comporta? (faixa, média, variabilidade, tendência)
- Quais sensores se **correlacionam** com o alvo? (candidatos a boas features)
- Onde estão os **faltantes** e os **outliers**?
- Há **multicolinearidade** (sensores muito correlacionados entre si)?

Ferramentas: `df.describe()`, `df.isna().mean()`, gráfico de linha do alvo, e a
**matriz de correlação** (heatmap). Correlação mede relação **linear** entre -1 e 1;
não captura relações não lineares, então é um ponto de partida, não a palavra final.

## Prática / Exercícios

Em `meu_trabalho/02_eda.py`, **escreva você**:

1. `describe()` do alvo e de cada sensor. O que a média e o desvio dizem?
2. Percentual de faltantes por coluna (`df.isna().mean()*100`). Onde está pior?
3. Matriz de correlação com heatmap (`seaborn.heatmap`). Quais 3 sensores mais se
   relacionam com a pureza? O sinal (positivo/negativo) faz sentido físico?
4. (Desafio) Crie um gráfico do alvo no tempo e marque visualmente os ciclos de
   manutenção (quedas + recuperações).

## Perguntas de fixação
1. Por que correlação alta com o alvo é **bom**, mas correlação alta **entre dois
   sensores** pode ser um problema?
2. A matriz de correlação capturaria uma relação em formato de "U" (não linear)?
   Por quê?
3. Como você explicaria, numa entrevista, por que fez EDA antes de treinar o modelo?

## Checkpoint
Você tem um script de EDA que lista faltantes, mostra a distribuição do alvo e uma
matriz de correlação interpretada. Avance para o **Módulo 03**.
