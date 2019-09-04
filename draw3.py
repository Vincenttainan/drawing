import turtle
from itertools import cycle


color=cycle(['red','orange','yellow','green','light blue','blue','purple'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next (color))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+1,shift+1,angle+1)


turtle.bgcolor('black')
turtle.speed('fastest')
turtle.pensize('4')
draw_circle(0,0,0)
