import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import *


def jaccard(l1, l2):
    interseccion = len(set(l1).intersection(set(l2)))
    union = len(set(l1).union(set(l2)))
    return interseccion / union


conta = 0
x = np.array(np.arange(0, 720))

x2 = np.array(np.arange(0, 720))
aux = []
aux2 = []
aux3 = []
errores1 = []
errores2 = []
errores3 = []
archivo = open("Itatira.csv")
archivo2 = open("Quixada.csv")
i = 0
for linea in archivo:
    s = linea.split(";")
    aux.append(float(s[2]))

fx = np.array(aux)

for linea in archivo2:
    s = linea.split(";")
    aux2.append(float(s[2]))

fx2 = np.array(aux2)
# Parte 1
# Interpolación Hermite
px = PchipInterpolator(x, fx)

muestras = 1000
a = np.min(x)
b = np.max(x)
p_x = np.linspace(a, b+1, muestras)
pfx = px(p_x)
for i in range (len(p_x)):
    p_x[i] = round(p_x[i], 2)
pfx = px(p_x)
for i in range (len(pfx)):
    pfx[i] = round(pfx[i], 2)
    
print("Valor f(0) interpolacion Hermite: ")
print(pfx[0])
print("Valor f(720) interpolacion Hermite: ")
print(pfx[720])
print()

j1 = jaccard(fx, pfx)
# Calculo de los errores
for p in range(720):
    errores1.append(abs((fx[p] - pfx[p]) / fx[p]))

plt.plot(x, fx, label="Datos originales Itatira", linewidth=0.8, color="k")
plt.plot(p_x, pfx, color="tab:red",
         label="Interpolacion Hermite Itatira", linewidth=0.8)
plt.legend()
plt.title("Datos reales vs interpolacion Hermite")
plt.xlabel("Indices Ideales")
plt.ylabel("Temperaturas")
plt.show()

# Interpolacion spline cúbica
px = CubicSpline(x, fx)

muestras = 1000
a = np.min(x)
b = np.max(x)
p_x = np.linspace(a, b+1, muestras)
pfx = px(p_x)
for i in range (len(p_x)):
    p_x[i] = round(p_x[i], 2)
pfx = px(p_x)
for i in range (len(pfx)):
    pfx[i] = round(pfx[i], 2)

    
print("Valor f(0) interpolacion spline cubica: ")
print(pfx[0])
print("Valor f(720) interpolacion spline cubica: ")
print(pfx[720])
print()
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
px = PchipInterpolator(x2, fx2)
muestras = 1000
a = np.min(x2)
b = np.max(x2)
p_x = np.linspace(a, b+1, muestras)
for i in range (len(p_x)):
    p_x[i] = round(p_x[i], 2)
pfx = px(p_x)
for i in range (len(pfx)):
    pfx[i] = round(pfx[i], 2)

    
print("Valor f(0) interpolacion Quixada: ")
print(pfx[0])
print("Valor f(720) interpolacion Quixada ")
print(pfx[720])
print()

j3 = jaccard(fx, pfx)
# Calculo de los errores
for p in range(720):
    errores3.append(abs((fx[p] - pfx[p]) / fx[p]))

plt.plot(x2, fx, label="Datos Itatira", linewidth=0.8, color="k")
plt.plot(p_x, pfx, color="tab:green",
         label="Datos interpolados Quixada", linewidth=0.8)
plt.legend()
plt.title("Datos Itatira vs interpolados Quixada")
plt.xlabel("Indices Ideales")
plt.ylabel("Temperaturas")
plt.show()



# Errores parte 1
for p in range(720):
    if errores1[p] == max(errores1):
        maxi = p
        break
    
for p in range(720):
    if errores1[p] == min(errores1):
        mini = p
        break
print("Errores parte 1 interpolacion Hermite: ")
print()
print("Error Maximo", round(max(errores1), 4), " en indice", maxi)
print("Error Minimo", round(min(errores1), 4), " en indice ", mini)
print("Error Medio", round((sum(errores1) / len(errores1)), 4))
print("Indice de Jaccard: ", round(j1, 4))
print()
for p in range(720):
    if errores2[p] == max(errores2):
        maxi = p
        break
    
for p in range(720):
    if errores2[p] == min(errores2):
        mini = p
        break
print("Errores parte 1 interpolacion spline cubica: ")
print()
print("Error Maximo", round(max(errores2), 4), " en indice", maxi)
print("Error Minimo", round(min(errores2), 4), " en indice", mini)
print("Error Medio", round((sum(errores2) / len(errores2)), 4))
print("Indice de Jaccard: ", round(j2, 4))
print()

#Errores parte 2


for p in range(720):
    if errores3[p] == max(errores3):
        maxi = p
        break
    
for p in range(720):
    if errores3[p] == min(errores3):
        mini = p
        break

print("Errores parte 2 Quixada ")
print()
print("Error Maximo", round(max(errores3), 4), " en indice", maxi)
print("Error Minimo", round(min(errores3), 4), " en indice", mini)
print("Error Medio", round((sum(errores3) / len(errores3)), 4))
print("Indice de Jaccard: ", round(j3, 4))
