
# String are immutable ##### U can think string is a tuble of character

# greeting = 'Hello, world!'
# greeting[0] = 'J' # that can't edit
# this is error

# just create a new string
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)