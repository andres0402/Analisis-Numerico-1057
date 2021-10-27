import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import *


def jaccard(l1, l2):
    interseccion = len(set(l1).intersection(set(l2)))
    union = len(set(l1).union(set(l2)))
    return interseccion / union


conta = 0
x = np.array(np.arange(1, 721))
x2 = np.array(np.arange(1, 297))
aux = []
aux2 = []
aux3 = []
errores1 = []
errores2 = []
errores3 = []
archivo = open("Itatira.csv")
archivo2 = open("Santa Quiteria.csv")
i = 0
for linea in archivo:
    s = linea.split(";")
    aux.append(float(s[2]))
    if i <= 295:
        aux3.append(float(s[2]))
    i += 1

fx = np.array(aux)
fx3 = np.array(aux3)

for linea in archivo2:
    s = linea.split(";")
    aux2.append(float(s[2]))

fx2 = np.array(aux2)
# Parte 1
# Interpolación lineal
px = interp1d(x, fx)

muestras = 1000
a = np.min(x)
b = np.max(x)
p_x = np.linspace(a, b, muestras)
pfx = px(p_x)

j1 = jaccard(fx, pfx)
# Calculo de los errores
for p in range(720):
    errores1.append(abs((fx[p] - pfx[p]) / fx[p]))

plt.plot(x, fx, label="Datos originales Itatira", linewidth=0.8, color="k")
plt.plot(p_x, pfx, color="tab:red",
         label="Interpolacion lineal Itatira", linewidth=0.8)
plt.legend()
plt.title("Datos reales vs interpolacion lineal")
plt.xlabel("Indices Ideales")
plt.ylabel("Temperaturas")
plt.show()

# Interpolacion spline cúbica
px = CubicSpline(x, fx)

muestras = 1000
a = np.min(x)
b = np.max(x)
p_x = np.linspace(a, b, muestras)
pfx = px(p_x)

j2 = jaccard(fx, pfx)
# Calculo de los errores
for p in range(720):
    errores2.append(abs((fx[p] - pfx[p]) / fx[p]))

plt.plot(x, fx, label="Datos originales Itatira", linewidth=0.8, color="k")
plt.plot(p_x, pfx, color="tab:red",
         label="Spline cubica Itatira", linewidth=0.8)
plt.legend()
plt.title("Datos reales vs spline cubica")
plt.xlabel("Indices Ideales")
plt.ylabel("Temperaturas")
plt.show()


# Parte 2
px = interp1d(x2, fx2)
muestras = 1000
a = np.min(x2)
b = np.max(x2)
p_x = np.linspace(a, b, muestras)
pfx = px(p_x)

j3 = jaccard(fx, pfx)
# Calculo de los errores
for p in range(296):
    errores3.append(abs((fx[p] - pfx[p]) / fx[p]))

plt.plot(x2, fx3, label="Datos Itatira", linewidth=0.8, color="k")
plt.plot(p_x, pfx, color="tab:green",
         label="Datos interpolados Santa Quiteria", linewidth=0.8)
plt.legend()
plt.title("Datos Itatira vs interpolados Santa Quiteria")
plt.xlabel("Indices Ideales")
plt.ylabel("Temperaturas")
plt.show()


# Errores parte 1
print("Errores parte 1 interpolacion lineal: ")
print()
print("Error Maximo", max(errores1))
print("Error Minimo", min(errores1))
print("Error Medio", sum(errores1) / len(errores1))
print("Indice de Jaccard: ", j1)
print()
print("Errores parte 1 interpolacion spline cubica: ")
print()
print("Error Maximo", max(errores2))
print("Error Minimo", min(errores2))
print("Error Medio", sum(errores2) / len(errores2))
print("Indice de Jaccard: ", j2)
print()

#Errores parte 2

print("Errores parte 2 Santa Quiteria: ")
print()
print("Error Maximo", max(errores3))
print("Error Minimo", min(errores3))
print("Error Medio", sum(errores3) / len(errores3))
print("Indice de Jaccard: ", j3)
