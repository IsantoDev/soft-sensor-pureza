import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados/sensores_coluna_destilacao.csv')

print(df.describe())
print(df.isna().mean()*100)

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt = '.2f', cmap='RdBu_r', center=0)
plt.title('Mapa de Correlação Sensores e pureza do Produto')
plt.tight_layout()
plt.show()