import numpy as np
import matplotlib.pyplot as mp
from math import log2,fabs

def rightRect(f,x,h):
    return f(x+h)

def middleRect(f,x,h):
    return f(x + h/2)

def Simpsons(f,x,h):
    return (f(x) + 4 * f(x + h / 2) + f(x + h)) / 6.0

def integration(f,a,b,n,rule):
    h=(b-a)/n
    return h*sum(rule(f,a+i*h,h) for i in range(n))


n = [2**i for i in range(0,20)]
x = [i for i in range(0,20)]
I=0.15614604126
a=0.
b=12.


IRR=[integration(np.sin,a,b,n[i],rightRect) for i in range(0,len(n))]
IMR=[integration(np.sin,a,b,n[i],middleRect) for i in range(0,len(n))]
# ISM=[Simpson(np.sin,a,b,n[i]) for i in range(0,len(n))]
ISM2=[integration(np.sin,a,b,n[i],Simpsons) for i in range(0,len(n))]

YR=[log2(fabs(IRR[i] - I)) for i in range(0,len(n))]
YM=[log2(fabs(IMR[i] - I)) for i in range(0,len(n))]
YS2=[log2(fabs(ISM2[i] - I)) for i in range(0,len(n))]


mp.xlabel("i")
mp.ylabel("log2(I-I*)")
mp.plot(x,YR,color="r",)
mp.plot(x,YM,color="b")
mp.plot(x,YS2,color="g")
mp.grid(True)
mp.show()
