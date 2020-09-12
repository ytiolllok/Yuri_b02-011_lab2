import turtle as t
k = 10
t.speed(1000)
def circle():
    a = 2
    for i in range(180):
        t.fd(a)
        t.lt(a)
for i in range(k):
    t.lt(360/k)
    circle()

