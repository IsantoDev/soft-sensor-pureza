# Módulo 05 — Split temporal e vazamento de dados

## Objetivo
Entender o erro mais comum (e mais punido em entrevista) em séries temporais: **split
aleatório**. Aprender a dividir treino/validação/teste **respeitando o tempo**.

## Teoria

Em problemas comuns, `train_test_split(shuffle=True)` é o padrão. Em **série
temporal, isso está ERRADO** e causa **vazamento de dados (data leakage)**:

- Se você embaralha, o modelo treina com pontos do **futuro** e é testado no
  **passado**. A métrica fica ótima no papel e o modelo **falha em produção**, porque
  na vida real você nunca tem o futuro.
- A regra: **treino = passado, teste = futuro**. Você corta a série por **tempo**:
  - Treino: primeiros 70%
  - Validação: 15% seguintes (para ajustar/escolher modelo)
  - Teste: últimos 15% (avaliação final, "futuro" que o modelo nunca viu)

No nosso caso, o teste é o período **mais recente** — com mais incrustação acumulada.
Isso é ótimo: testa se o modelo generaliza para condições novas, não para um trecho
"fácil" sorteado do meio.

Outras formas de vazamento a evitar:
- Imputar ou normalizar usando estatísticas do **conjunto inteiro** (incluindo teste)
  antes de separar. O correto é ajustar no treino e **aplicar** no teste.
- Usar features que olham o futuro (`shift` negativo) — visto no Módulo 04.

Para validação mais robusta existe o `TimeSeriesSplit` do scikit-learn (validação
cruzada que respeita o tempo) — bom conhecer o nome para a entrevista.

## Prática / Exercícios

Em `meu_trabalho/05_split.py`, **escreva você**:

1. Defina `X` (todas as features) e `y` (`pureza_produto`).
2. Calcule os índices de corte: 70% e 85% do total.
3. Fatie `X_treino/X_val/X_teste` e `y_*` por **posição** (`.iloc`), sem embaralhar.
4. Imprima as **datas** de início e fim de cada conjunto para provar que não há
   sobreposição temporal.

## Perguntas de fixação
1. Explique, com suas palavras, por que embaralhar uma série temporal vaza dados.
2. Por que faz sentido o **teste** ser o período mais recente?
3. Cite outra forma de vazamento além do split aleatório.

## Checkpoint
Você divide os dados por tempo, sem vazamento, e consegue **defender** por que isso é
obrigatório. Avance para o **Módulo 06**.
