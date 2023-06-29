import turtle as t
def draw_square(length):
    for i in range(4): t.forward(length); t.left(90)
for i in range(4): draw_square(int(input("enter square length: ")))
t.exitonclick()