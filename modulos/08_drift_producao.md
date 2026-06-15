# Módulo 08 — Monitoramento em produção (drift)

## Objetivo
Entender que **treinar um modelo é só metade do trabalho**. Em produção, o mundo muda
e o modelo precisa ser monitorado e retreinado.

## Teoria

**Data drift** (desvio de dados): a distribuição dos dados de entrada muda com o
tempo. No nosso caso, a incrustação progride, a operação muda de setpoint, estações
do ano chegam. O modelo treinado ontem pode ser ruim amanhã.

**Como detectar drift:**
1. **Monitorar o erro** (se você tem feedback do laboratório): calcule o erro médio
   móvel. Se disparar acima de um limiar, é sinal de retreino.
2. **Monitorar as features** (sem feedback): compare a distribuição das entradas no
   treino vs. hoje. Métricas como PSI (Population Stability Index) ou teste KS.

**Estratégia simples para o nosso caso:**
- Calcule o **erro absoluto médio móvel de 24h** no período de "produção" (teste).
- Defina um **limiar de alerta** = média + 2 × desvio do erro no treino.
- Se o erro móvel cruzar o limiar → dispara retreino.

Isso é exatamente o que empresas fazem em produção real, e mostrar que você sabe disso
diferencia você na entrevista.

## Prática / Exercícios

Em `meu_trabalho/08_drift.py`, **escreva você**:

1. Calcule o erro absoluto entre previsto e real no conjunto de teste.
2. Calcule a **média móvel de 24h** desse erro.
3. Defina o limiar (média + 2×desvio) e plote o erro móvel com linha de alerta.
4. (Análise) Em que momento o modelo "pede" retreino? O que estava acontecendo no
   processo nesse período?

## Perguntas de fixação
1. O que é **data drift** e por que ele acontece no nosso problema?
2. Por que monitorar o erro médio móvel em vez do erro pontual?
3. Como você **saberia** que é hora de retreinar sem ter o laboratório medindo em
   tempo real?

## Checkpoint
Você tem um gráfico de monitoramento com limiar de alerta e consegue explicar a
lógica de retreino. Avance para o **Módulo 09**.
