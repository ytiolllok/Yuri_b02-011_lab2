import random
from random import randint
import turtle as t
t.penup()
t.goto(-200,-200)
t.pendown()
t.goto(-200,200)
t.goto(200,200)
t.goto(200,-200)
t.goto(-200,-200)
t.ht()
t.penup()
numt = 50
def random_speed():
    vx = random.uniform(-5,5)
    vy = ((25-vx**2)**0.5)*(random.choice([1,-1]))
    return[vx, vy]
pool = [t.Turtle(shape='circle') for i in range(numt)]
speed = [random_speed() for i in range(numt)]
speedlist = list(speed)
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
for unit in pool:
    unit.lt(randint(-180,180))
while(True):
    for i in range(numt):
        if (pool[i].xcor() + speed[i][0] > 200):
            speed[i][0] = -1*speed[i][0]
        if (pool[i].xcor() + speed[i][0] < -200):
            speed[i][0] = -1*speed[i][0]
        if (pool[i].ycor() + speed[i][1] > 200):
            speed[i][1] = -1*speed[i][1]
        if (pool[i].ycor() + speed[i][1] < -200):
            speed[i][1] = -1*speed[i][1]
        pool[i].goto(pool[i].xcor() + speed[i][0], pool[i].ycor() + speed[i][1])

