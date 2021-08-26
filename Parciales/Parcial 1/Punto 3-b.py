#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Punto 3-b
import math

def f(x):
    return x-math.cos(x)

def g(x):
    return math.cos(x)

def puntoFijo(E):
    #100 iteraciones
    iteraciones = 100
    #Intervalo [0,2]
    a = 0
    b = 2
    conta = 1
    b = g(a)
    
    error = abs(b-a)
    while(error > E and conta < iteraciones):
        b = g(a)
        error = abs(b-a)
        a = b
        conta += 1
    if(conta >= iteraciones):
        print("Diverge")
    else:
        return b

print("Solucion aproximada: ", puntoFijo(10**-5))
    


# In[ ]:





# In[ ]:




