import matplotlib.pyplot as plt
import numpy as np

etiquetas = ["Original", "Optimizado"]
tiempos = [23.5390, 0.0006]

plt.figure(figsize=(8, 6))
plt.bar(etiquetas, tiempos, color=['red', 'green'])
plt.title("Comparativa de Tiempos de Ejecución")
plt.ylabel("Segundos")
plt.yscale('log')

plt.text(0, 23.5390, "23.539 s", ha='center', va='bottom')
plt.text(1, 0.0006, "0.0006 s", ha='center', va='bottom')

plt.savefig('grafico_final.png')
print("Gráfico guardado como 'grafico_final.png'")
plt.show()
