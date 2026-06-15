# Módulo 06 — Modelagem com scikit-learn

## Objetivo
Treinar modelos de regressão, comparar com um **baseline realista** e entender por que
"o mais complexo" nem sempre vence.

## Teoria

Antes de qualquer modelo sofisticado, você precisa de um **baseline**: a estimativa
mais simples que um ser humano faria sem ML. Se o seu modelo não supera o baseline,
não serve.

**Nosso baseline:** sem soft sensor, o operador usa a **última medição de laboratório**
disponível — que ocorre a cada 8 horas. Entre uma medição e outra, ele repete o último
valor. O soft sensor tem que ganhar disso para se justificar.

Modelos que vamos testar:
- **Regressão Linear** — assume relação linear entre features e alvo. Simples,
  interpretável, mas pode subajustar (underfitting) se a relação for não linear.
- **Random Forest** — conjunto de árvores de decisão, captura não linearidades.
  Robusto, mas pode superajustar (overfitting) e é caixa-preta.
- **Gradient Boosting** — árvores em sequência, cada uma corrige o erro da anterior.
  Em geral bate o RF, mas mais sensível a hiperparâmetros.

Fluxo do scikit-learn: `modelo.fit(X_treino, y_treino)` → `modelo.predict(X_teste)`.

## Prática / Exercícios

Em `meu_trabalho/06_modelos.py`, **escreva você**:

1. Crie o baseline (última medição de lab a cada 8h, forward fill).
2. Instancie e treine os 3 modelos. Use `random_state=42` onde aplicável.
3. Para cada modelo, calcule **MAE, RMSE e R²** no conjunto de teste.
4. Monte uma tabela comparativa (pode ser um DataFrame) ordenada por RMSE.
5. (Análise) Qual modelo ganhou? O resultado te surpreende? Por quê?

## Perguntas de fixação
1. Por que usamos um baseline e não comparamos modelos entre si diretamente?
2. O que é **overfitting** e como o split temporal nos protege dele?
3. Se a Regressão Linear ganhou do Random Forest neste problema, qual seria uma
   hipótese para isso?

## Checkpoint
Você tem uma tabela de métricas comparando baseline e 3 modelos, e consegue
interpretar os números e defender as escolhas. Avance para o **Módulo 07**.
