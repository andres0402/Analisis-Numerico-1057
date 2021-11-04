#!/usr/bin/env python
# coding: utf-8

# In[6]:


from scipy import integrate
import math
f= lambda x: x*(math.e**x)
print("Cuadratura de Gauss para :(1,2)x^e(x) (Resultado, error)")
qua1=integrate.quadrature(f,1.0,2.0)
print(qua1,"\n")

print("Cuadratura de Gauss para :(1,1.5)x^e(x)")
qua2=integrate.quadrature(f,1.0,1.5,args=(),tol=1e-01 ,rtol=1e-01)
print(qua2,"\n")
print("Cuadratura de Gauss para :(1.5,2)x^e(x)")
qua3=integrate.quadrature(f,1.5,2)
print(qua3,"\n")

print("Particion (1,1.5)x^e(x)+(1.5,2)x^e(x):")
qua4=qua2[0]+qua3[0]
print(qua4)


# In[ ]:




