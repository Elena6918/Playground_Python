import turtle

t = turtle.Turtle()
t.speed('fastest')

def flower(t, time, size):
    if time == 0:
        t.circle(size, 180)
    else:
        for i in range(4):
            flower(t, time - 1, size / 2)
            t.left(90)
        flower(t, time - 1, size / 2)
        t.left(180)

flower(t, 5, 500)
turtle.done()