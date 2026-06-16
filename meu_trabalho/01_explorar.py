import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados/sensores_coluna_destilacao.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp').sort_index()

plt.plot(df.index, df['pureza_produto'])

plt.title('Pureza do Produto ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Pureza (%)')

for lag in [1,6,24]:
    print(f'Autocorrelação com lag {lag}h: {df["pureza_produto"].autocorr(lag=lag):.4f}')
plt.show()


