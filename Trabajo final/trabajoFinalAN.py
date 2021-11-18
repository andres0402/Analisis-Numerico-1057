import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sympy as sp
plt.style.use("bmh")

x,y,z = sp.symbols('x,y,z')

def derive(f,nd):
    t=f
    for j in range(1,nd+1):
        d=sp.diff(f.subs(y,y(x)),x)
        f = d.subs(sp.Derivative(y(x),x),t).subs(y(x),y)
    return f

def taylor(f,a,b,h,m,k):
    u = np.zeros([m,2])
    D = [ ]
    for j in range(1,k+1):
        D = D+[derive(f,j)]
    for i in range(m):
        g = f.subs(x,a).subs(y,b)
        t = b+h*g
        for j in range(1,k+1):
            z = D[j-1].subs(x,a).subs(y,b)
            t = float(t+h**(j+1)/sp.factorial(j+1)*z)
        b=t
        a=a+h
        u[i,0]=a
        u[i,1]=b
    return u

# Las ecuaciones diferenciales del modelo SIR
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * C0 * I / N
    dIdt = beta * S * C0 * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def plot(S, I, R, t, divide_by=1):
    # Dibujamos los datos de S(t), I(t) y R(t)
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    ax.plot(t, R / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel(f'Número (dividido por {divide_by:,})')
    legend = ax.legend()
    print("")
    # fig.show()
    
def plot_with_death_rate(S, I, R, t, divide_by=1, death_rate=0.05):
    # Dibujamos los datos de S(t), I(t) y R(t)
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    RR = R * (1 - death_rate)
    DD = R - RR
    ax.plot(t, RR / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.plot(t, DD / divide_by, 'k', alpha=0.5, lw=2, label='No recuperado')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel(f'Número (dividido por {divide_by:,})')
    legend = ax.legend()
    print("")
    # fig.show()
    
# población inicial, N.
N = 479000 # poblaciçon de un país como España
 
# Número inicial de infectados y recuperados, I0 and R0.
I0 = 2/N
R0 = 0
C0 = 1.5
 
# El resto, casi todo N, es susceptible de infectarse
S0 = N - 1 - I0

 
# Tasas de contagio y recuperación.
beta = 0.06 # contagio
gamma = 0.021 # recuperación
 
# Pasos temporales (en días)
t = np.linspace(0, 652, 652)
t2 = np.linspace(0, 10, 10)
 
# condiciones iniciales
y0 = S0, I0, R0
ySM = S0, 14/N, 7/N #Condiciones iniciales para Santa Marta

#Solucion inicial 
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

#Solucion Santa Marta
ret2 = odeint(deriv, ySM, t2, args=(N, beta, gamma))
S2, I2, R2 = ret2.T

for i in range(len(I)):
    if I[i] == max(I):
        print("Porcentaje de la poblacion infectada: ", round(I[i]/N, 4))
        print("Dia: ", i+1)
        

for i in range(len(R)):
    if R[i] == max(R):
        print("Porcentaje de la poblacion infectada: ", round(R[i]/N, 4))
        print("Dia: ", i+1)


# print(I)

# taylor(deriv,a,b,1,365,3)
 
# plot(S, I, R, t) # Datos sin normalizar

#plot(S, I, R, t, divide_by=N) # Datos normalizados

#plot(S2, I2, R2, t2, divide_by=N)

relativoS = 0
absolutoS = 0
relativoI = 0
absolutoI = 0
relativoR = 0
absolutoR = 0
relativosS = []
absolutosS = []
relativosI = []
absolutosI = []
relativosR = []
absolutosR = []

for i in range (10):
    error = abs((S[i] - S2[i])/S2[i])
    error2 = abs(S[i] - S2[i])
    relativoS += error
    relativosS.append(error)
    absolutosS.append(error2)
    absolutoS += error2
    error = abs((I[i] - I2[i])/I2[i])
    error2 = abs(I[i] - I2[i])
    relativoI += error
    relativosI.append(error)
    absolutosI.append(error2)
    absolutoI += error2
    error = abs((R[i] - R2[i])/R2[i])
    error2 = abs(R[i] - R2[i])
    relativoR += error
    relativosR.append(error)
    absolutosR.append(error2)
    absolutoR += error2

print()
print("Errores relativos: ")
print("Error relativo medio susceptibles: ", abs(relativoS/10))
print("Error relativo medio infectados: ", abs(relativoI/10))
print("Error relativo medio recuperados: ", abs(relativoR/10))
print()
print("Errores absolutos: ")
print("Error absoluto medio susceptibles: ", abs(absolutoS/10))
print("Error absoluto medio infectados: ", abs(absolutoI/10))
print("Error absoluto medio recuperados: ", abs(absolutoR/10))
print()


t3 = np.linspace(0, 10, 10)



plt.plot(t3, relativosS, label = "Susceptible")
plt.plot(t3, relativosI, label = "Infectados", color = "tab:red")
plt.plot(t3, relativosR, label = "Recuperados con inmunidad", color = "tab:green")
plt.title("Errores relativos")
plt.xlabel("Tiempo/dias")
plt.ylabel("Error relativo")
plt.legend()
plt.show()



    

plt.plot(t3, absolutosS, label = "Susceptible")
plt.plot(t3, absolutosI, label = "Infectados", color = "tab:red")
plt.plot(t3, absolutosR, label = "Recuperados con inmunidad", color = "tab:green")
plt.legend()
plt.title("Errores absolutos")
plt.xlabel("Tiempo/dias")
plt.ylabel("Error absoluto")
plt.show()


ret2 = odeint(deriv, ySM, t, args=(N, beta, gamma))
S2, I2, R2 = ret2.T


for i in range(len(S)):
    if int(S[i]) == 111450:
        ind = i
        break

print("Error relativo para Re(t) = 1.001: ", abs((S[ind] - S2[ind])/S2[ind]))



for i in range(len(S)):
    if int(S[i]) == 168961:
        ind = i
        break

    
print("Error relativo para Re(t) = 1.5: ", abs((S[ind] - S2[ind])/S2[ind]))


for i in range(len(S)):
    if int(S[i]) == 215494:
        ind = i
        break
    
print("Error relativo para Re(t) = 1.9: ", abs((S[ind] - S2[ind])/S2[ind]))

for i in range(len(S)):
    if int(S[i]) == 281147:
        ind = i
        break
    
print("Error relativo para Re(t) = 2.5: ", abs((S[ind] - S2[ind])/S2[ind]))


#Gráfica punto 2
plot_with_death_rate(S, I, R, t, divide_by=N, death_rate=0.05)