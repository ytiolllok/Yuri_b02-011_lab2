import turtle as t
co1 = (0,0)
co2 = (0,30)
co3 = (0,60)
co4 = (30,60)
co5 = (30,30)
co6 = (30,0)
si0 = [co1, co2, co3, co4, co5, co6, co1]
si1 = [co2, co4, co5, co6]
si4 = [co3, co2, co5, co4, co6]
si7 = [co1, co2, co4, co3]
index = [si1, si4, si1, si7, si0, si0]
test = [si0, si0]
xcor = -100
t.speed(1)
t.color('blue')
def digit(cords):
    global xcor
    t.penup()
    t.goto(cords[0][0]+xcor, cords[0][1])
    t.pendown()
    for x, y in cords:
        t.goto(x+xcor, y)
    t.penup()
def post(number):
    for i in number:
        global xcor
        digit(i)
        t.penup()
        xcor += 60
t.penup()
post(index)

