#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Punto 1.e
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp
import pandas as pd

def newton_raphson (E, k):
  conver = []
  errores = []
  its = []
  x = sp.Symbol('x')  
  fx = x**3+2*x+k
  f = sp.lambdify(x, fx)
  deriv = fx.diff(x)
  x0 = 2
  it = 0
  error = abs(10*E)
  while(error > E):
    x1 = x0 - (f(x0)/deriv.subs(x, x0))
    conver.append(x1)
    error = abs(x1 - x0)
    errores.append(abs((x1-x0)/x1))
    x0 = x1
    it += 1
    its.append(it)
  return x1, it, conver, errores, its


#Tomando k=0+sqrt(k+2)
res, it, conver, errores, its = newton_raphson(10**-12, math.sqrt(2))

print("Solucion aproximada con k = sqrt(2): ", res)
print("Numero de iteraciones ", it)

plt.plot(its, conver)
plt.title('Convergencia')
plt.ylabel('X1')
plt.xlabel('Iteracion')
plt.show()
df = pd.DataFrame()


#Tomando k=0-(1/3)
res, it, conver, errores2, its2 = newton_raphson(10**-12, (-1/3))

print("Solucion aproximada con k = -1/3): ", res)
print("Numero de iteraciones ", it)

plt.plot(its2, conver)
plt.title('Convergencia')
plt.ylabel('X1')
plt.xlabel('Iteracion')
plt.show()

df["Iteracion"] = its2
df["Error relativo"] = errores2
print(df)




# In[ ]:




