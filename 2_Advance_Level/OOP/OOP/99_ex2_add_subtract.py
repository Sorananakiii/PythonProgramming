
# The most basic vector operations we want our Point object to handle are addition and subtraction
# Exercise 2: add_subtract
# For two points  (𝑥1,𝑦1)+(𝑥2,𝑦2)=(𝑥1+𝑥2,𝑦1+𝑦2)  and similarly for subtraction
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, number):
        if isinstance(number, Point):
            return Point(self.x + number.x, self.y + number.y)
        else:
            raise TypeError('Expected number to be int or Rational. Got %s' % type(number))

    def __sub__(self, number):
        if isinstance(number, Point):
            return Point(self.x - number.x, self.y - number.y)
        else:
            raise TypeError('Expected number to be int or Rational. Got %s' % type(number))

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

p = Point(2,4)
print(p - 1)