from abc import ABC, abstractmethod


# Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass


# Leaf
class Circle(Graphic):
    def draw(self):
        print("Draw circle")


# Leaf
class Square(Graphic):
    def draw(self):
        print("Draw square")


# Composite
class Image(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

    def draw(self):
        print("Draw image")
        for graphic in self.graphics:
            graphic.draw()


# Client
image = Image()
image.add(Circle())
image.add(Square())
picture = Image()
picture.add(image)
picture.add(Image())
picture.draw()


"""
Compose objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of objects uniformly.
"""