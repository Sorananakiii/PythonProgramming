
# This implicit tuple comes up most often when working with functions that return multiple outputs
# For example, we might have a function that returns the first and last letter of a string
def first_last(s):
    return s[0], s[-1]

chars = first_last('hello!')
print(chars)


# In such cases, we'll sometimes want to store the multiple outputs in separate variables.

first_char, last_char = first_last('hello!')

print(first_char)
print(last_char)