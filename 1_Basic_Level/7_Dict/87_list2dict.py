

# `zip`
# The `zip` function can be very handy for creating a `dict`. 
# Let's go back to the `list` we made before that contained all the values describing me. 
# We'll make a second `list` containing all the keys we would want for putting these values in a dictionary

value_list = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]
key_list = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']

print(value_list)
print(key_list)

key_value_pairs = list(zip(key_list, value_list))
print(key_value_pairs)

me_dict = dict(key_value_pairs)
print(me_dict)