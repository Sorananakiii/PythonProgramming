
# Instead of Create external object
# use __int__ functional to build a object
class tutorial:

    def __init__(self, first, last, subject):
        self.first = first
        self.last = last
        self.subject = subject

        # self.name = first + ' ' + last
        # or build function
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


tor_1 = tutorial('prayet', 'jungg', 'mathmatic')
tor_2 = tutorial('somchai', 'jungg', 'physic')

print()
print(tor_1.subject)
print(tor_2.subject)
print(tor_1.fullname())

# class Circle():
#     is_shape = True
#
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#
# first_circle = Circle(2, 'blue')
# ---> __init__(self , radius, color) but self argument is not need a value
# second_circle = Circle(3, 'red')
# print('color of first circle is [{}]'.format(first_circle.color))
# print('radius of first circle is [{}]'.format(first_circle.radius))
#
# print('color of 2nd circle is [{}]'.format(second_circle.color))
# print(first_circle.is_shape)
# first_circle.color = 'Black'
# print('color of first circle is [{}]'.format(first_circle.color))