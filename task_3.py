class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = width if height is None else height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


    def __add__(self, other):
        list_s = sorted([self.width, self.height, other.width, other.height])
        new_width = list_s[0] + list_s[3]
        new_height = list_s[1] + list_s[2]
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        new_width = self.width - other.width
        new_height = self.height - other.height
        if new_height > 0 and new_width > 0:
            return Rectangle(new_width, new_height)
        return f'Данная операция не может быть выполнена так, как одна из сторон равна нулю или имеет отрицательное значение'

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'




if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)
    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")
    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
