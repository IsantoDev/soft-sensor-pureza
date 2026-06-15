# Módulo 01 — Fundamentos de séries temporais

## Objetivo
Dominar a teoria mínima de séries temporais que a vaga exige: **tendência,
sazonalidade, defasagem (lag), autocorrelação e dados faltantes**. Sem isso, o resto
da trilha é decoreba.

## Teoria

Uma **série temporal** é uma sequência de observações ordenadas no tempo, em geral
com espaçamento regular (aqui: 1 leitura por hora). A ordem **importa** — não dá para
embaralhar como numa tabela comum.

Os componentes clássicos:

- **Tendência (trend):** movimento de longo prazo, para cima ou para baixo. No nosso
  caso, a incrustação (*fouling*) derruba a pureza ao longo dos dias — até a limpeza
  da coluna, quando recupera. Padrão recorrente em **dente-de-serra**.
- **Sazonalidade:** padrão que se repete em período fixo. Aqui, o **ciclo diário** de
  temperatura ambiente (dia quente / noite fria) influencia o processo.
- **Defasagem (lag):** o valor de `t` horas atrás. `lag1` = valor de 1h atrás. Lags
  capturam a **memória** do processo (inércia térmica).
- **Autocorrelação:** correlação da série **com ela mesma** defasada. Se a pureza de
  agora se parece muito com a de 1h atrás, há forte autocorrelação de lag 1 — sinal de
  que lags serão boas features.
- **Estacionariedade:** uma série é estacionária quando suas propriedades (média,
  variância) não mudam ao longo do tempo. Tendência e sazonalidade **quebram** a
  estacionariedade. Muitos métodos assumem estacionariedade; saber identificar isso é
  meio caminho.
- **Dados faltantes:** sensores falham. Em série temporal, faltantes têm tratamento
  especial (não dá para simplesmente jogar a média) — assunto do Módulo 03.

## Prática / Exercícios

Crie `meu_trabalho/01_explorar.py`. **Escreva você** o código (peça dicas ao tutor, não
a solução):

1. Carregue o CSV com `pandas`, transforme `timestamp` em índice datetime e ordene.
2. Plote a série da `pureza_produto` no tempo. **Identifique a olho** onde está a
   tendência e onde está a sazonalidade.
3. Calcule a **autocorrelação** da pureza nos lags 1, 6 e 24 horas. Dica: use
   `series.autocorr(lag=k)`. Interprete: qual lag tem mais "memória"?
4. (Teórico, responda em texto no topo do arquivo como comentário) A série da pureza é
   estacionária? Justifique citando os componentes que você identificou.

## Perguntas de fixação
1. Qual a diferença entre **tendência** e **sazonalidade**? Dê um exemplo de cada na
   nossa planta.
2. Por que **não** podemos embaralhar uma série temporal antes de treinar um modelo?
3. O que a **autocorrelação de lag 1** alta nos diz sobre quais features criar?

## Checkpoint
Você sabe definir os 6 conceitos acima com suas palavras e apontar cada um no gráfico
da pureza. Peça as perguntas de verificação ao tutor antes de ir ao **Módulo 02**.
