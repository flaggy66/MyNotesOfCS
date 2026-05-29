from demo04.shape import Shape, Circle

shape = Shape("large", "red")
print(type(shape))
print(shape)
print(shape.appearance.size, shape.appearance.color)
shape.draw()

shape.appearance.changeSize("small")
shape.draw()

shape.size = "medium"
shape.draw()

shape.appearance.changeColor("yellow")
shape.draw()

print("----------")

circle = Circle("small","blue",4,(0,0))
circle.draw()
area = circle.area
print(area)