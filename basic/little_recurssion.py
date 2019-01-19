import turtle

t = turtle.Turtle()
t.speed('fastest')

def flower_basket(t, time, size):
    if time == 0:
        t.circle(size, 180)
    else:
        for i in range(4):
            flower_basket(t, time - 1, size / 2)
            t.left(90)
        flower_basket(t, time - 1, size / 2)
        t.left(180)
flower_basket(t, 5, 500)

def flower(t, time, size, angle):
    if time == 0:
        for i in range(4):
            t.circle(size, 180)
            t.left(90)
    else:
        flower(t, time - 1, size, angle)
        t.left(90)
        flower(t, time - 1, size, angle)
        t.right(angle)

flower(t, 5, 50, 30)
turtle.done()


