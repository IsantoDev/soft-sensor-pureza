# Trilha de Estudo — Soft Sensor Industrial com Séries Temporais

Estudo guiado, **prático e teórico**, que termina na construção de um projeto de
ciência de dados aplicado à indústria: um **soft sensor** que estima a pureza de um
produto em uma coluna de destilação a partir de sensores baratos, usando Python e
scikit-learn.

**Objetivo:** fechar os gaps de *machine learning, séries temporais e estatística
aplicada* e ter uma peça de portfólio que você **entende e sabe defender** — pensado
para a vaga de Ciência de Dados da Radix.

---

## Como usar com o Claude Code

1. Abra esta pasta no **Claude Code** (`claude` no terminal, dentro do diretório).
2. O Claude Code lê o `CLAUDE.md` e passa a atuar como **seu tutor**: ele te guia,
   te faz escrever o código, dá dicas em vez de respostas e checa seu entendimento
   antes de avançar.
3. Comece dizendo: *"Vamos começar o módulo 00"* — e siga a ordem dos módulos.
4. Escreva **seu** código na pasta `meu_trabalho/`. O tutor revisa de lá.

> O `GABARITO/` existe só para conferência **depois** de você tentar. Resista a abrir
> antes — o ganho está na tentativa, não na resposta pronta.

---

## Setup (uma vez)

```bash
pip install -r requirements.txt
python dados/gerar_dados.py     # gera dados/sensores_coluna_destilacao.csv
```

---

## Mapa da trilha

| Módulo | Tema | Teoria / Prática |
|---|---|---|
| 00 | Setup e o problema do soft sensor | Teoria |
| 01 | Fundamentos de séries temporais | Teoria + exercícios |
| 02 | EDA e qualidade de dados | Prática |
| 03 | Tratamento de dados faltantes | Teoria + prática |
| 04 | Engenharia de features temporais | Teoria + prática |
| 05 | Split temporal e vazamento de dados | Teoria + prática |
| 06 | Modelagem com scikit-learn | Teoria + prática |
| 07 | Avaliação e diagnóstico | Teoria + prática |
| 08 | Monitoramento em produção (drift) | Teoria + prática |
| 09 | Montagem do projeto final + defesa | Projeto |

Ao fim, você terá o pipeline completo escrito **por você**, um README próprio e
respostas ensaiadas para a entrevista.

---

## Estrutura

```
soft-sensor-estudo/
├── CLAUDE.md              # instruções do tutor (o Claude Code lê)
├── README.md             # este arquivo
├── requirements.txt
├── dados/
│   └── gerar_dados.py    # gerador dos dados (já pronto)
├── modulos/              # a trilha, 00 a 09
├── meu_trabalho/         # VOCÊ escreve seu código aqui
└── GABARITO/             # referência — só conferir depois de tentar
```
