import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as legend
from math import log2,fabs

def rightRect(f,x,h):
    return f(x+h)

def middleRect(f,x,h):
    return f(x + h/2)

def Simpson(f,x,h):
    return (f(x) + 4 * f(x + h / 2) + f(x + h)) / 6.0

def integration(f,a,b,n,rule):
    h=(b-a)/n
    return h*sum(rule(f,a+i*h,h) for i in range(n))


n = [2**i for i in range(0,20)]
x = [i for i in range(0,20)]
I=0.15614604126
a=0.
b=12.


Right = [log2(fabs(integration(np.sin,a,b,n[i],rightRect)-I)) for i in range(0,len(n))]
Middle = [log2(fabs(integration(np.sin,a,b,n[i],middleRect)-I)) for i in range(0,len(n))]
Sim = [log2(fabs(integration(np.sin,a,b,n[i],Simpson)-I)) for i in range(0,len(n))]

mp.xlabel("iterations")
mp.ylabel("log2(I-I*)")
mp.plot(x,Right,color="r",label="RightRect")
mp.plot(x,Middle,color="lightblue")
mp.plot(x,Sim,color="g")

mp.legend(handles = [legend.Patch(color="r",label="Right Rect"),
                     legend.Patch(color="lightblue", label="Middle Rect"),
                     legend.Patch(color="g", label="Simpson")])

mp.show()
