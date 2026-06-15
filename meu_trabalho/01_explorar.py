import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados/sensores_coluna_destilacao.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp').sort_index()

plt.plot(df.index, df['pureza_produto'])

plt.title('Pureza do Produto ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Pureza (%)')
plt.show()
