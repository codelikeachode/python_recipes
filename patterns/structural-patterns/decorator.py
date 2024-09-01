from abc import ABC, abstractmethod


# Component
class IShape(ABC):
    # Operation
    @abstractmethod
    def show_info(self):
        pass


# ConcreteComponent
class Square(IShape):
    def show_info(self):
        print("square")


# Decorator
class ShapeDecorator(IShape):
    def __init__(self, shape):
        self.shape = shape

    # Operation
    def show_info(self):
        self.shape.show_info()


# ConcreteDecorator
class ColorSharp(ShapeDecorator):
    def __init__(self, shape, color):
        super().__init__(shape)
        self.color = color

    def show_info(self):
        print(self.color + " ")
        self.shape.show_info()


# ConcreteDecorator
class ShadowShape(ShapeDecorator):
    def show_info(self):
        self.shape.show_info()
        print("with shadow")


# Client
square = Square()
square.show_info()
# printed: square

colorShape = ColorSharp(square, "red")
colorShape.show_info()
# printed: red square

shadowShape = ShadowShape(colorShape)
shadowShape.show_info()
# printed: red square with shadow


"""
Attach additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.
"""
