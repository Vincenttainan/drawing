import turtle as t
def rectangle(horizontal,vertical):
    t.penup()
    t.shape('turtle')
    t.pensize(1)
    t.begin_fill()
    t.speed('fastest')
    for counter in range(1,3):
        t.pendown()
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
x=0
for counter in range(1,10000):
    x=x+5
    t.goto(0-x,x)
    rectangle(x,0-x)
    t.goto(x,0-x)
    rectangle(0-x,x)
