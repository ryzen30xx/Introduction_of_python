import turtle as t
color = ["white", "black", "blue", "red", "yellow"]; radius = 100
def circle_at(x, y, radius, colour):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    t.setheading(0)
    t.circle(radius)
    t.end_fill()
for i in color: circle_at(0, 0, radius, i); radius = radius - 20
t.exitonclick()