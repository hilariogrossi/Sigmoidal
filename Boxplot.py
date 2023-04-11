# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Importar dados para o Dataframe
df = pd.read_csv(
    'https://raw.githubusercontent.com/carlosfab/dsnp2'
    '/master/datasets/dengue-dataset.csv')

# Ver as 5 primeiras
print(df.head())

# Plotar o Boxplot para as temperaturas
df.boxplot(['temperatura-media', 'temperatura-mininima', 'temperatura-maxima'])
plt.show()

# Plotar o Boxplot para casos confirmados
df.boxplot(['casos-confirmados'], vert=False)
plt.show()

