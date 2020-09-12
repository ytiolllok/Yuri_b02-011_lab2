import numpy as np
import turtle as t
k = 15
r = 10
n = 3
def figure(r,n):
    angle = 180*(n - 2)/n
    a = r*2*np.sin(np.pi/n)
    t.penup()
    t.fd(r)
    t.pendown()
    t.lt(180 - angle/2)
    for i in range(n):
        t.fd(a)
        t.lt(180 - angle)
    t.lt(angle/2)
    t.penup()
    t.fd(r)
    t.lt(180)
    
for i in range(k):
    figure(r,n)
    r += 10
    n += 1
