# The dict is also mutable. 
# We can add new key-value pairs by simple assignment.

me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}
me_dict['favorite book'] =  'The Little Prince'
print(me_dict)


# We can also use update, similar to the way we used it for a set, except now with key-value pairs.
me_dict.update({'favorite color': 'orange', 'siblings': 3, 'nieces/nephews': 3})
print(me_dict)