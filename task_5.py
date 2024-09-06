import abc
from math import pi, sqrt


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return float(f"{pi * self.radius ** 2:.2f}")


class Rectangle:
    def __init__(self, width, height=None):
        super().__init__()
        self.width = width
        self.height = width if height is None else height

    def area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return float(f'{sqrt(p*(p - self.a)*(p-self.b)*(p-self.c)):.2f}')


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 8, 9)
    # Вычисление площади фигур
    circle_area = circle.area()
    rectangle_area = rectangle.area()
    triangle_area = triangle.area()
    # Вывод результатов
    print("Площадь круга:", circle_area)
    print("Площадь прямоугольника:", rectangle_area)
    print("Площадь треугольника:", triangle_area)
    # shape = Shape()

