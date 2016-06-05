import numpy as np

def rightRect(f,x,h):
    return f(x+h)

def middleRect(f,x,h):
    return f(x + h/2)

def Simpson(f,a,b,n):
    h = (b - a) / n
    return h/6*sum(f(a+(i-1)*h)+4*f(a+i*h)+f(a+(i+1)*h) for i in range(1,n-1))

def integration(f,a,b,n,rule):
    h=(b-a)/n
    return h*sum(rule(f,a+i*h,h) for i in range(n))


n = [2**i for i in range(1,20)]
a=0.
b=12.
# for i in range(0,len(n)):
#     print "N: %10d,     Integral method: %15s,         result: %5.30f"%(
#     n[i],rightRect.__name__,integration(np.sin,a,b,n[i],rightRect))
#     print "N: %10d,     Integral method: %15s,         result: %5.30f" % (
#     n[i], middleRect.__name__, integration(np.sin, a, b, n[i], middleRect))
#     print "N: %10d,     Integral method: %15s,         result: %5.30f" % (
#     n[i],"Simpson", Simpson(np.sin,a,b,n[i]))

# print "N: %10d,     Integral method: %15s,         result: %5.30f" % (
#     2**22,"Simpson", Simpson(np.sin,a,b,2**21))
print "N: %10d,     Integral method: %15s,         result: %5.30f" % (
    2**21,"Simpson", Simpson(np.sin,a,b,2**21))