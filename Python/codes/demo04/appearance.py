class Appearance:
    """外观类"""

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def changeSize(self, size):
        self.size = size

    def changeColor(self, color):
        self.color = color
