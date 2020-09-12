import turtle as t
a = 10
for n in range(10):
    for i in range(4):
        t.fd(a)
        t.lt(90)
    t.rt(135)
    t.penup()
    t.fd(a*2**0.5)
    t.pendown()
    t.lt(135)
    a*=3
