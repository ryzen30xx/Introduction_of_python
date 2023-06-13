import turtle as t
useroptions = str(input("What geometries do you want to draw: "))
if useroptions not in ["triangle", "square"]: print("wrong request!"); exit()
elif useroptions == "triangle": 
    for i in range(3): t.forward(50); t.left(120)
elif useroptions == "square":
    for i in range(4): t.forward(50); t.left(90)