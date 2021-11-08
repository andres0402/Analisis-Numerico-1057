from sympy import*
from scipy import integrate
import numpy as np

def f2(x, y):
    #res = []
    m = np.array([[0, 0, 4, 6, 0], [0, 3, 5, 7, 3], [1, 5, 6, 9, 5], [0, 2, 3, 5, 1], [0, 0, 1, 2, 0]])
    iy = int((2*y)/100)
    ix = (x/100).astype(int)  
    res = m[iy, ix]
    return res
    
def simpson(fun, a, b, n):
    if n % 2 == 1:
        raise ValueError("N debe ser un numero par.")
    dx = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = fun(x)
    sol = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return sol

def simpson2(fun2, ax, bx, ay, by, mx, my):
    x = Symbol('x')
    dy = (by-ay)/my
    v = ay
    r = []
    for i in range(0, my+1):
        def g(x):
            return fun2(x, v)
        u = simpson(g, ax, bx, mx)
        r += [u]
        v += dy
    s = 0
    for i in range(1, my):
        s = s+2*(2-(i+1)%2)*r[i]
    s = dy/3*(r[0]+s+r[my])
    return s


resultado = round(simpson2(f2, 0, 400, 0, 200, 4, 4), 2)
print("El volumen aproximado de agua es de", resultado, "metros cubicos")