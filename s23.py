# string = "me and sara and nikan are friends."
# word = ''
# all_words = []
# for char in string:
#     word += char
#     if char == ' ' or char == '.':
#         all_words.append(word[:-1])
#         word =''

# print(all_words)

import turtle

s = turtle.Screen()

p = turtle.Pen()
p.penup()

p.goto(-100, 20)
p.pendown()
p.goto(100, 20)
p.left(120)
p.forward(200)
p.left(120)
p.forward(200)

p.penup()

p.goto(-100, -20)
p.setheading(0)
p.pendown()
p.forward(200)


s.exitonclick()
