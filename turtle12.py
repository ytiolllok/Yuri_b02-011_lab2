import turtle as t
def circle(r):
    a= 2
    for i in range(90):
        t.fd(a*r)
        t.lt(a)
for i in range(15):
    circle(1)
    circle(0.1)
