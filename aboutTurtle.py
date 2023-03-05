import turtle
s = turtle.Screen()
s.bgcolor('orange')
s.register_shape('strawberry.gif')
# s.bgpic('mario.png')
p = turtle.Pen()
# p.shape('square')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
p.shape('strawberry.gif')
p.shapesize(1.2)
p.pensize(4)
p.pencolor('red')
p.fillcolor('green')
p.begin_fill()
# draw triangle
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.end_fill()
p.forward(100)
p.right(120)
p.forward(100)
p.right(120)
p.forward(100)
p.right(120)
s.exitonclick()


# exercise 1
# یک مربع بکشید
# یک پنجضلعی توپر با رنگ آبی بکشید
# یک شش ضلعی بکشید
