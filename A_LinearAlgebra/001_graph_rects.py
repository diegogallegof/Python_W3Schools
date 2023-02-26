import matplotlib.pyplot as plt

# Definir las ecuaciones
eq1 = lambda x: (-1)*x - 7
eq2 = lambda x: (-2/2)*x - 13/5

# Generar los puntos para las líneas
x_vals = range(-5, 6)
y_vals1 = [eq1(x) for x in x_vals]
y_vals2 = [eq2(x) for x in x_vals]

# Graficar las líneas
plt.plot(x_vals, y_vals1, label='x-y=7')
plt.plot(x_vals, y_vals2, label='2x-2y=14')

# Personalizar el gráfico
plt.title('Rectas')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.legend()

# Mostrar el gráfico
print(y_vals1)
print(y_vals2)
print(x_vals)
plt.show()
