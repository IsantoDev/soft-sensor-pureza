# Módulo 04 — Engenharia de features temporais

## Objetivo
Transformar sensores "crus" em features que dão ao modelo **memória** e **contexto**
temporal: lags, janelas móveis e variáveis de calendário.

## Teoria

Um modelo de regressão comum vê cada linha isolada. Mas no nosso processo o estado
agora depende do passado recente. **Engenharia de features** injeta esse contexto:

- **Lags:** `sensor_lag1`, `sensor_lag2`, `sensor_lag3` = valor de 1, 2 e 3 horas
  atrás. Dão ao modelo a "memória" da inércia do processo. Criados com `.shift(k)`.
- **Janelas móveis (rolling):**
  - `media_movel_6h = sensor.rolling(6).mean()` → **nível** recente (suaviza ruído).
  - `desvio_movel_6h = sensor.rolling(6).std()` → **volatilidade** recente (o processo
    está estável ou agitado?).
- **Features de calendário:** `hora` e `dia_da_semana` extraídos do índice. Capturam a
  **sazonalidade** diária/semanal de forma explícita.
- **Variável operacional:** `horas_desde_manutencao` já vem nos dados. Ela é o
  **proxy direto da incrustação** — provavelmente a feature mais forte. (Pense: por que
  o modelo precisa dela e não consegue "adivinhar" a incrustação só pelos sensores
  instantâneos?)

⚠️ **Atenção ao vazamento (leakage):** `.shift(k)` com `k` **positivo** olha para o
**passado** (correto). Nunca use `shift(-k)` (futuro) como feature — isso vaza o
amanhã para dentro do modelo.

Criar lags e janelas gera `NaN` nas **primeiras linhas** (não há passado suficiente).
Essas linhas devem ser descartadas com `dropna()` **depois** de criar as features.

## Prática / Exercícios

Em `meu_trabalho/04_features.py`, **escreva você**:

1. Para cada sensor, crie lags de 1, 2 e 3 horas com um laço e `.shift()`.
2. Para cada sensor, crie média e desvio móveis de 6h.
3. Crie `hora` e `dia_semana` a partir do índice.
4. Faça `dropna()` e conte quantas linhas sobraram. Quantas features você tem agora?
5. (Teórico) Por que descartamos as primeiras linhas em vez de preencher com zero?

## Perguntas de fixação
1. Para que serve um **lag** e o que ele representa fisicamente aqui?
2. Qual a diferença, em informação, entre a **média móvel** e o **desvio móvel** de 6h?
3. Por que `shift(-1)` como feature seria um **erro grave**?

## Checkpoint
Você tem uma matriz de features (com dezenas de colunas) construída por você, sem
vazamento, e sabe explicar o papel de cada tipo de feature. Avance para o
**Módulo 05**.
