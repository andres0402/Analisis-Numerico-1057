
#SERIES DE TAYLOR

import numpy as np
from tabulate import tabulate



def Taylor (xi, h, n):    #Tabla comparativa Taylor y grafico error
  fx_i = fx(xi)           #Asignamos el vector que contiene la funcion f(x_i) y sus derivadas
  fx_i11 = fx(x_ii)[0]    #Valor real de f(x_i+1)
  T = []                  #terminos de la serie de taylor
  Fty = []                #Suma de los terminos de la serie de taylor
  Res = []                #Residual
  Er = []                 #Error relativo
  Orden = []              #Numeracion del orden
  Taylor_table = []
  for i in range(n + 1):
    T.append(fx_i[i] * (h**i) / np.math.factorial(i))       
                                                            
    if i == 0:
      Fty.append(T[i])
    else:
      Fty.append(T[i] + Fty[i-1])                           
    
    Res.append(fx_i11 - Fty[i])                             

    Er.append(Res[i]*100 / fx_i11)                           

    Orden.append(i)                                         

    Taylor_table.append([Orden[i], Fty[i], Res[i], Er[i]])


  print(tabulate(Taylor_table, headers = ["Orden", "f(x_(i+1))", "Rn", "e(%)"]))

  # Grafica fx y aproximaciones
  import matplotlib.pyplot as plt

  plt.plot(Orden, Er, label=("Error %"))

  plt.plot()                      #llamando grafica 

  plt.xlabel("x axis")            #Etiqueta de eje
  plt.ylabel("y axis")            #Etiqueta de eje
  plt.title("Grado del polinomio Vs Error %") #Titulo del grafico
  plt.legend()                    #Leyendas
  plt.show()                      #Mostrar grafico

  return ()

def Taylorf (xi, h, n):   
  fx_i = fx(xi)           
  fx_i11 = fx(x_ii)[0]    
  T = []                  
  Fty = []                
  Res = []                
  Er = []                 
  Orden = []              
  Taylor_table = []
  for i in range(n + 1):
    T.append(fx_i[i] * (h**i) / np.math.factorial(i)) 
    if i == 0:
      Fty.append(T[i])
    else:
      Fty.append(T[i] + Fty[i-1])                           #Genera la suma de los terminos de la Serie de Taylor
    
    Res.append(fx_i11 - Fty[i])                             #Residual

    Er.append(Res[i]*100 / fx_i11)                           #Error relativo (%)

    Orden.append(i)                                         #Numeracion del orden

  return (Fty)

x_i = 0           #Valor inicial de x = x_i
x_ii = 1         #Valor final de x = x_(i+1)
h = x_ii - x_i    #Incremento
n = 2             #Orden del polinomio de aproximacion

#Funcion a aproximar y sus derivadas

def fx (x):
  F=[]                                                                  #Vector de la funcion y sus derivadas
  F.append(2*(2**x)-0.009*(2**x))     #f(x)
  F.append(0.4*x-0.018*x)             #f'(x)
  F.append(-0.4-0.018)                #f''(x)   
  #Agregar las n-esimas derivadas que sean necesarias para la aproximacion
  return (F)

tabl = Taylor (x_i, h, n)
print(tabl)


# Grafica fx y aproximaciones
import matplotlib.pyplot as plt
delta = 100
xp = np.linspace(x_i, x_ii, delta)
hp = xp - x_i
yp = Taylorf(x_i, hp, n)
ypo = fx(xp)[0]
#print(yp[n])

for i in range(n+1):
  plt.plot(xp, yp[i], label=("orden " + str(i+1)))

plt.plot(xp, ypo, label=("f(x)"))

plt.plot()                      #llamando grafica 

plt.xlabel("x axis")            #Etiqueta de eje
plt.ylabel("y axis")            #Etiqueta de eje
plt.title("Grafica de la funcion") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico

def fx2 (x):
  F=[]                                                                  #Vector de la funcion y sus derivadas
  F.append(-0.4*(x**2)+0.0115(x**2))     #f(x)
  F.append(0.4*x-0.018*x)             #f'(x)
  F.append(-0.777)                #f''(x)   
  #Agregar las n-esimas derivadas que sean necesarias para la aproximacion
  return (F)

tabl = Taylor (x_i, h, n)
print(tabl)


# Grafica fx y aproximaciones
import matplotlib.pyplot as plt
delta = 100
xp = np.linspace(x_i, x_ii, delta)
hp = xp - x_i
yp = Taylorf(x_i, hp, n)
ypo = fx(xp)[0]
#print(yp[n])

for i in range(n+1):
  plt.plot(xp, yp[i], label=("orden " + str(i+1)))

plt.plot(xp, ypo, label=("f(x)"))

plt.plot()                      #llamando grafica 

plt.xlabel("x axis")            #Etiqueta de eje
plt.ylabel("y axis")            #Etiqueta de eje
plt.title("Grafica de la funcion") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico