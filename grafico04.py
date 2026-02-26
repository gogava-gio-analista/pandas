import matplotlib.pyplot as plt

x = ['atletico', 'real madrid', 'barcelona', 'sevilla']
y = [10, 20, 15, 5]


plt.pie(y, labels=x)
plt.title('Cantidad de títulos por equipo')
plt.savefig('images/pie.png')
plt.show()