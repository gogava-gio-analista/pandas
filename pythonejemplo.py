import pandas as pd 



datos = {
    'Nombre': ['Juan', 'María', 'Pedro'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(datos)
print(df)

dffiltrado = df[df['Edad'] > 28]
print(dffiltrado)

dfordenado = df.sort_values(by='Edad', ascending=False)
print(dfordenado)