#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd


def jacobi(A, b, tol, its, x0):
    D = np.diag(np.diag(A))
    LU = A - D
    iters = []
    xs = []
    x = x0
    for i in range (1, its):
        xs.append(x)
        iters.append(i)
        inv = np.linalg.inv(D)
        x0 = x
        x = np.dot(inv, b)-np.dot(inv, (np.dot(LU, x)))
        if np.linalg.norm(x - x0) < tol:
            return x, i, iters, xs
    return x, i, iters, xs
        


# In[14]:


def gaussSeidel(A, b, tol, its, x0):
   
    iteraciones = 1
    x = x0
    n = 3
    m = 3
    dif = np.ones(n, dtype = float)
    err = 2*tol
    for k in range (its):
        for i in range (n):
            suma = 0
            for j in range (n):
                    if j != i:
                        suma = suma + A[i][j]*x[j]
            x1 = (b[i] - suma)/A[i][i]
            dif[i] = abs(x1 - x[i])
            x[i] = x1
        err = np.max(dif)
        iters.append(iteraciones)
        iteraciones += 1
        if err < tol:
            return x, iteraciones
    return x, iteraciones


# In[15]:


#Se definen Alfa y Beta de tal forma que cumpla con que la matriz es diagonalmente dominante, de tal forma que ambos métodos convergen.
#Para este caso se define Alfa = 3 tal que sea mayor que abs(-1)+abs(1) = 2 y Beta = 0 tal que abs(Beta)+abs(-1) sea menor que abs(2)
alfa = 3
beta = 0
A = np.array([[2, 0, -1], [beta, 2, -1], [-1, 1, alfa]])
a = np.array([1, 2, 1])

D = np.diag(np.diag(A))
LU = A - D
#Matriz T
T = np.dot(np.linalg.inv(D), -LU)
vals = np.linalg.eig(T)
valProps = vals[0]


# In[16]:


#Se verifica si el método converge por el teorema de convergencia
for v in valProps:
    if abs(v) >= 1:
        print("La solucion no converge")
        break
x0 = np.zeros(3)
x, i, iters, sols = jacobi(A, a, 1e-10, 500, x0)
y, iteraciones = gaussSeidel(A, a, 1e-10, 500, x0)
print("Solucion con Jacobi: ", x)
print("Iteraciones: ", i)
print("Solucion con Gauss-Seidel: ", y)
print("Iteraciones: ", iteraciones)
print("Solucion con numpy: ", np.linalg.solve(A, a))
x0 = np.array([1, 2, 3])
x, i, iters, sols = jacobi(A, a, 1e-10, 500, x0)
print()
print("Tabla metodo Jacobi con x0 = [1, 2, 3]:")
df = pd.DataFrame()
df["Iteracion"] = iters
df["Vector x"] = sols
print(df)


# In[ ]:





# In[ ]:




