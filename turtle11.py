import turtle as t
r = 1
k = 5
t.speed(10000)
t.rt(90)
def circle(r):
    a= 2
    for i in range(180):
        t.fd(a*r)
        t.lt(a)
    t.lt(180)    
    for i in range(180):
        t.fd(a*r)
        t.lt(a)
for i in range(k):
    circle(r)
    r += 1
