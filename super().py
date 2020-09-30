class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):

    # def __init__(self,length):
    # self.length = length

    # def area(self):
    # return self.length * self.length

    # def perimeter(self):
    # return 4 * self.length
    def __init__(self, length):
        super().__init__(length, length)


sq = Square(5)

rec = Rectangle(7, 4)

print(sq.area())
print(rec.area())

print(sq.perimeter())
print(rec.perimeter())
