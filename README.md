# Soft Sensor Industrial — Estimativa de Pureza com Séries Temporais

Projeto de ciência de dados aplicado à indústria: um **soft sensor** que estima a
pureza de um produto em uma coluna de destilação a partir de sensores baratos
(temperatura, pressão, vazão), usando Python e scikit-learn.

## O problema

Em colunas de destilação industriais, medir a **pureza do produto** exige análise de
laboratório — cara e lenta. Sensores de temperatura, pressão e vazão, por outro lado,
são baratos e medem o tempo todo.

Um **soft sensor** é um modelo de ML que estima a variável cara (pureza) a partir das
variáveis baratas, em **tempo real**, substituindo o laboratório.

## Por que é série temporal?

Os dados chegam ordenados no tempo (1 leitura/hora) e o estado atual do processo
depende do passado recente (inércia térmica). Além disso, há:

- **Tendência:** incrustação (*fouling*) degrada a separação ao longo dos dias
- **Sazonalidade:** ciclo diário de temperatura ambiente afeta o processo
- **Dados faltantes:** sensores falham — tratamento especial necessário

## Stack

Python · pandas · scikit-learn · matplotlib · seaborn

## Setup

```bash
pip install -r requirements.txt
python dados/gerar_dados.py     # gera o dataset sintético
```

## Estrutura do projeto

| Módulo | Tema |
|---|---|
| 01 | Fundamentos de séries temporais |
| 02 | EDA e qualidade de dados |
| 03 | Tratamento de dados faltantes |
| 04 | Engenharia de features (lags, janelas móveis) |
| 05 | Split temporal e vazamento de dados |
| 06 | Modelagem com scikit-learn |
| 07 | Avaliação e diagnóstico |
| 08 | Monitoramento em produção (drift) |
| 09 | Pipeline final |

```
soft-sensor-pureza/
├── README.md
├── requirements.txt
├── dados/
│   └── gerar_dados.py    # gerador do dataset sintético
├── modulos/              # teoria e exercícios de cada módulo
├── meu_trabalho/         # scripts desenvolvidos durante o estudo
└── outputs/              # gráficos e métricas gerados
```
