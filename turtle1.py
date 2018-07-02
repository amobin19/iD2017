import turtle
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'pink', 'cyan']
t = turtle.Pen()
t.speed(100)
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x%8])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(90)
