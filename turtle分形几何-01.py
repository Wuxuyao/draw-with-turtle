import turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(100)
t.pencolor('indigo')
t.ht()
def basic(r):
    for i in range(1,3):
        t.fd(r)
        t.rt(20)
        t.fd(r)
        t.rt(160)
        t.fillcolor('indigo')
def flower(r):
    for i in range(1,37):
        basic(r)
        t.rt(10)
    while r <= 100:
        r = r + 10
        flower(r)
flower(50)







