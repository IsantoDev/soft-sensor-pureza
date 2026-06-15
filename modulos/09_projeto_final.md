# Módulo 09 — Montagem do projeto final e defesa

## Objetivo
Juntar tudo que você construiu nos módulos 02–08 em **um pipeline limpo e coeso**,
escrever o **seu** README e ensaiar a **defesa em entrevista**. Aqui o estudo vira
portfólio.

## Parte A — Refatorar para um pipeline único

Até agora você tem scripts soltos em `meu_trabalho/`. Um projeto de portfólio precisa
ser **organizado e reproduzível**. Crie `meu_trabalho/pipeline.py` que execute, em
ordem, tudo que você já escreveu:

1. Carga + EDA (Módulo 02)
2. Tratamento de faltantes (Módulo 03)
3. Engenharia de features (Módulo 04)
4. Split temporal (Módulo 05)
5. Modelagem + baseline (Módulo 06)
6. Avaliação + gráficos (Módulo 07)
7. Monitoramento de drift (Módulo 08)

Boas práticas que o tutor deve cobrar de você:
- Funções pequenas e nomeadas (`tratar_faltantes`, `criar_features`, `avaliar`...).
- Comentários explicando o **porquê** das decisões, não só o quê.
- Reprodutibilidade: `random_state` fixo; script roda do zero sem erro.
- Salvar gráficos em `outputs/` e a tabela de métricas em CSV.

> Só **depois** de ter sua versão rodando, compare com `GABARITO/pipeline_completo.py`.
> Não copie: use como conferência. Se algo seu ficou diferente e funciona, ótimo —
> entenda o trade-off.

## Parte B — Escreva o SEU README

Escreva `meu_trabalho/README.md` com: o problema, os dados, o pipeline, os resultados
(tabela de métricas + gráficos) e uma seção **"Decisões técnicas"**. Escreva com suas
palavras — é isso que prova que você entendeu.

## Parte C — Defesa em entrevista (o que mais importa)

Para **cada** pergunta abaixo, escreva sua resposta e depois defenda em voz alta para o
tutor, que vai te interromper e aprofundar (como um entrevistador da Radix faria):

1. Por que **split temporal** e não aleatório? O que é vazamento de dados?
2. Por que **interpolação por tempo** nos faltantes, e não a média? E em produção?
3. Para que servem **lags** e **janelas móveis**? Dê o significado físico.
4. Por que você comparou com um **baseline**? Qual era o baseline e por que ele é justo?
5. Por que a **Regressão Linear** ganhou das árvores neste problema?
6. O que é **R² negativo** e o que você faria se o visse?
7. Como você **monitoraria** esse modelo em produção? O que dispara um retreino?
8. Conte a **história do diagnóstico**: você notou um padrão nos resíduos. O que era e
   como resolveu? (dica: incrustação / feature de manutenção)

## Parte D — Publicação

1. Suba como repositório **público** no seu GitHub (`IsantoDev`), nome sugerido:
   `soft-sensor-pureza`.
2. Capriche no README (é a primeira coisa que recrutador e o André veem).
3. (Opcional) Escreva um post de LinkedIn curto contando o projeto e o aprendizado.

## Checkpoint final
Você consegue:
- [ ] Rodar seu pipeline do zero sem erro.
- [ ] Explicar cada etapa **sem olhar o código**.
- [ ] Responder às 8 perguntas de defesa com segurança e profundidade.
- [ ] Apontar uma limitação do projeto e um próximo passo concreto.

Quando marcar os quatro, você está pronto para a entrevista técnica da Radix. 🎯
