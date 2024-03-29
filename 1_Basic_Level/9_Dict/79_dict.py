# Dict

# A dictionary is like a list, but more general. In a list, the index positions have to
# be integers; in a dictionary, the indices can be (almost) any type.

# You can think of a dictionary as a mapping between a set of indices (which are
# called keys) and a set of values. Each key maps to a value. The association of a
# key and a value is called a key-value pair or sometimes an item.

# As an example, we’ll build a dictionary that maps from English to Spanish words,
# so the keys and the values are all strings.

# The function dict creates a new dictionary with no items. Because dict is the
# name of a built-in function, you should avoid using it as a variable name.

eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
print(len(eng2sp))

# this doesn't work
# invalid_dict = {[1, 5]: 'a', 5: 23}
# print(invalid_dict)

print('one' in eng2sp)
print('uno' in eng2sp)