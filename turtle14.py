import turtle as t
import numpy as np
def star(n):
    angle = (180-180/n)
    a = 200*np.sin(180-180/n)
    for i in range(n):
        t.fd(a)
        t.lt(angle)
star(5)
t.up()
t.fd(100)
t.down()
star(11)
