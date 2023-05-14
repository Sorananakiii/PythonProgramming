
# Exercise 3: multiplication
# define scalar multiplication given a point  𝑃  and a scalar  𝑎  as 𝑎𝑃=𝑎(𝑥,𝑦) = (𝑎𝑥,𝑎𝑦)
# and
# define the inner product for points  𝑃,𝑄  as 𝑃⋅𝑄=(𝑥1,𝑦1)⋅(𝑥2,𝑦2) = 𝑥1𝑥2 + 𝑦1𝑦2

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, number):
        if isinstance(number, int):
            return Point(number * self.x, number * self.y)
        elif isinstance(number, Point):
            return number.x * self.x + number.y * self.y
        else:
            raise TypeError('Expected number to be int or Rational. Got %s' % type(number))

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

def mult_result(points):
    points = [Point(*point) for point in points]
    return [point*point*2 for point in points]