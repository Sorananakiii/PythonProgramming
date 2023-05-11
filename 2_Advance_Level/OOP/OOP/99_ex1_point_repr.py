
# Exercise 1: point_repr
#
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)


point = Point(2, 3)
print(point)