# string

# string is a sequence of characters.
# You can access the characters one at a time with the bracket operator
# But the string index started counting at zero, the six letters are numbered 0 to 5. 
# To get the last character, you have to subtract 1 from length

fruit = 'banana'
first_char = fruit[0]
last_char = fruit[len(fruit)-1]

print(fruit)
print(len(fruit))
print(first_char)
print(last_char)
