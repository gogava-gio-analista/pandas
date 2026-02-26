import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/datos.csv', delimiter=';')
print(df.head(8))

diccionario = df.to_dict(orient='records')
for elemento in diccionario:
    print(elemento)

dfmedia = df['edad'].mean()
print(f'La edad media es: {dfmedia}')

df_grupo = df.groupby('ocupacion')['ocupacion'].count()
print(df_grupo)

figura, eje = plt.subplots()
eje.bar(df_grupo.index, df_grupo.values)
eje.set_xlabel('Ocupación')
eje.set_ylabel('Cantidad')
eje.set_title('Cantidad de personas por ocupación')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()