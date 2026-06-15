# Módulo 00 — Setup e o problema do soft sensor

## Objetivo
Entender **o que** você vai construir e **por que** isso importa para a vaga da Radix,
e deixar o ambiente pronto.

## Teoria — o problema

Imagine uma **coluna de destilação** numa indústria química. A variável que mais
importa é a **pureza do produto** que sai da coluna. O problema: medir pureza exige
**análise de laboratório** — cara e lenta (resultado sai horas depois).

Por outro lado, a planta tem dezenas de **sensores baratos** medindo o tempo todo:
temperatura, pressão, vazão. Esses dados existem de sobra.

Um **soft sensor** (sensor virtual) é um **modelo** que estima a variável cara
(pureza) a partir das variáveis baratas (temperaturas, pressões, vazões), em tempo
real. É um problema clássico de **regressão** aplicado à **indústria** — exatamente o
que a descrição da vaga cita: *soft sensors, predição de falhas, otimizadores de
processo*.

Por que isso é **série temporal** e não uma regressão comum?
- Os dados chegam ordenados no tempo, a cada hora.
- O estado agora depende do estado das horas anteriores (inércia do processo).
- Há **tendência** (a coluna incrusta e perde eficiência), **sazonalidade** (ciclo
  diário) e **dados faltantes** (sensores falham).

Esses quatro pontos — tendência, sazonalidade, defasagem e faltantes — são os
fundamentos de séries temporais que você vai dominar nesta trilha.

## Prática

1. Instale as dependências e gere os dados:
   ```bash
   pip install -r requirements.txt
   python dados/gerar_dados.py
   ```
2. Abra `dados/gerar_dados.py` e **leia** (não precisa escrever — trate como "os dados
   que a empresa te entregou"). Observe quais sensores existem e qual é o alvo.

## Perguntas de fixação (responda ao tutor)
1. Em uma frase, o que é um soft sensor e por que uma indústria iria querer um?
2. Qual é a **variável-alvo** do nosso problema e por que ela é "cara" de medir?
3. Por que tratamos isso como série temporal, e não como uma tabela qualquer?

## Checkpoint
Você consegue explicar o problema para alguém leigo em 30 segundos, deixando claro o
valor de negócio (substituir lab caro por estimativa em tempo real). Quando
conseguir, peça ao tutor para liberar o **Módulo 01**.
