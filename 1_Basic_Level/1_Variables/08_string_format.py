# basic string formatting
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#  need to write a format string which prints out the data using
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)