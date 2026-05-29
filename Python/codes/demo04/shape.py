from demo04.appearance import Appearance


class Shape:
    """形状类"""

    def __init__(self, size, color):
        self.appearance = Appearance(size, color)
        self.area = 0

    def draw(self):
        print(f"This shape: size is {self.appearance.size}, color is {self.appearance.color}.")


class Circle(Shape):
    """圆形类"""

    def __init__(self, size, color, radius, center):
        super().__init__(size, color)
        self.radius = radius
        self.center = center
        self.area = 3.14 * (radius ** 2)

    def draw(self):
        print(
            f"This shape is Circle: radius is {self.radius}, "
            f"center is {self.center}, size is {self.appearance.size}, color is {self.appearance.color}.")
