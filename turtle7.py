import turtle as t
t.speed(10000000)
def spiral(k,n):
    a = 0
    for i in range(n*360):
        t.fd(k*((1+a**2)**0.5))
        t.lt(1)
        a+=1
spiral(0.001,2)
 
