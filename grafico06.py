import matplotlib.pyplot as plt

dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')
temperaturas = []
# pedir las temperaturas de cada día
for dia in dias:
    temp = float(input(f'Ingrese la temperatura del {dia}: '))
    temperaturas.append(temp)

plt.plot(dias, temperaturas, label='semana1')
temperaturas2 = [23, 25, 22, 24, 26]
plt.plot(dias, temperaturas2, label='semana2')
plt.title('Temperaturas de la semana')
plt.xlabel('Días')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.savefig('images/temperaturas1.png')
plt.show()