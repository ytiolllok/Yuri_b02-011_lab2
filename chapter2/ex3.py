import turtle as t
# test = [si0, si0]
t.speed(1)
t.color('blue')
f = open('config.txt', 'r')
co1 = list(map(int, f.readline().split(',')))
co2 = list(map(int, f.readline().split(',')))
co3 = list(map(int, f.readline().split(',')))
co4 = list(map(int, f.readline().split(',')))
co5 = list(map(int, f.readline().split(',')))
co6 = list(map(int, f.readline().split(',')))
si0 = [co1, co2, co3, co4, co5, co6, co1]
si1 = [co2, co4, co5, co6]
si2 = [co3, co4, co5, co1, co6]
si3 = [co3, co4, co2, co5, co1]
si4 = [co3, co2, co5, co4, co6]
si5 = [co1, co6, co5, co2, co3, co4]
si6 = [co4, co2, co1, co6, co2]
si7 = [co1, co2, co4, co3]
si8 = [co1, co2, co3, co4, co5, co6, co1, co2, co5]
si9 = [co1, co5, co4, co3, co2, co5] 
index = [si1, si4, si1, si7, si0, si0]
print(co1)
print(co2)
print(co3)
print(co4)
print(co5)
print(co6)
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
