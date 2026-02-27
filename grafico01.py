import matplotlib.pyplot as plt

x = ['atletico', 'real madrid', 'barcelona', 'sevilla']
y = [10, 20, 15, 5]


plt.bar(x, y)
plt.title('Cantidad de títulos por equipo')
plt.xlabel('Equipos')
plt.ylabel('Cantidad de títulos')
plt.savefig('images/barra.png')
plt.show()