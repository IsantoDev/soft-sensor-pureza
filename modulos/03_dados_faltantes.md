# Módulo 03 — Tratamento de dados faltantes

## Objetivo
Aprender as estratégias de imputação e escolher a **certa para séries temporais**,
sabendo justificar a escolha.

## Teoria

Sensores falham: leituras viram `NaN`. Você tem opções:

1. **Remover linhas com faltante (`dropna`)** — simples, mas em série temporal
   abre **buracos no tempo** e descarta dados bons das outras colunas. Raramente ideal.
2. **Imputar pela média/mediana** — fácil, mas **ignora a ordem temporal**: preenche um
   buraco às 3h da manhã com a média do mês inteiro, achatando a dinâmica. Ruim para
   séries.
3. **Forward fill (`ffill`)** — repete o último valor válido. Bom para sinais que mudam
   devagar, mas "congela" durante o buraco.
4. **Interpolação por tempo (`interpolate(method="time")`)** — estima o valor faltante
   na **reta entre os vizinhos**, respeitando o espaçamento temporal. Em geral é a
   melhor escolha para sensores contínuos, porque honra a continuidade física do
   processo.

Regra prática para o nosso caso: **interpolação por tempo** para os sensores +
`ffill`/`bfill` para cobrir faltantes nas **pontas** (início/fim da série, onde a
interpolação não tem os dois vizinhos).

⚠️ **Cuidado com vazamento:** ao imputar, use só informação disponível "naquele
momento". Métodos que usam o futuro (como interpolação) são aceitáveis para limpar o
histórico de treino, mas em produção, em tempo real, você só tem o passado — então o
`ffill` é o que roda ao vivo. Saber dessa nuance impressiona numa entrevista.

## Prática / Exercícios

Em `meu_trabalho/03_faltantes.py`, **escreva você**:

1. Conte os faltantes antes do tratamento.
2. Aplique `interpolate(method="time")` nos sensores e depois `ffill().bfill()`.
   Confirme que zerou os faltantes.
3. (Comparação) Pegue **um** sensor, crie duas versões — uma imputada pela média,
   outra por interpolação temporal — e plote as duas sobre o trecho da falha em bloco
   da pressão (linhas ~1000–1013). Qual preserva melhor a dinâmica? Comente.

## Perguntas de fixação
1. Por que imputar pela **média** é geralmente ruim em série temporal?
2. Qual a diferença entre `ffill` e `interpolate(method="time")`?
3. Em **produção**, em tempo real, qual desses métodos você consegue usar e por quê?

## Checkpoint
Seu dataset está sem faltantes, com a estratégia escolhida **justificada**. Avance
para o **Módulo 04**.
