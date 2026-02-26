import matplotlib.pyplot as plt

x = ['atletico', 'real madrid', 'barcelona', 'sevilla']
y = [10, 20, 15, 5]


plt.plot(x, y)
plt.title('Cantidad de títulos por equipo')
plt.xlabel('Equipos')
plt.ylabel('Cantidad de títulos')
plt.savefig('images/lineas.png')
plt.show()