import turtle as t
useroptions = str(input("What geometries do you want to draw: "))
if useroptions in ["triangle", "square"]:
    if useroptions == "triangle": 
        for i in range(3): t.forward(50); t.left(120)
    elif useroptions == "square":
        for i in range(4): t.forward(50); t.left(90)
else: print("wrong request!")