import matplotlib.pyplot as plt

productos = []
ventas = []

# pedir 5 productos y sus ventas
for i in range(5):
    producto = input(f'Ingrese el nombre del producto {i+1}: ')
    venta = float(input(f'Ingrese las ventas del producto {i+1}: '))
    productos.append(producto)
    ventas.append(venta)

# crear gráfico de pie
plt.pie(ventas, labels=productos, autopct='%1.1f%%')
plt.title('Ventas de productos')
plt.savefig('images/ventas_productos.png')
plt.show()