import turtle


s = turtle.Screen()
p = turtle.Pen()
p.shape('turtle')
p.speed('fast')
p2 = turtle.Pen()
p2.speed('normal')

p2.forward(150)


p.penup()
p.pendown()
COLORS = ['red', 'green', 'cyan', 'yellow']
for i in range(4):
    p.fillcolor(COLORS[i])
    p.begin_fill()
    for i in range(4):
        p.forward(100)
        p.right(90)
    p.left(90)
    p.end_fill()


p.penup()
p.goto(-80, 130)
p.write("Our Nice squares", font=16)
p.ht()
s.exitonclick()
