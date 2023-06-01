
# Variables and names are not the same thing in python. 
# For instance, run the following code

a = 4
b = a
print(a, b)

# assigned the name a to the value 4 and then b to be equal to a.
# But, b does not point to a, it points to the variable that has the name a.
# Thus, assigning the name b to the value of a does not cause the value of b to change when the value of a changes.

a = 5
print(a, b)

