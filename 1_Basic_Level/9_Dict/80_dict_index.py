# Dict have no index

me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}
print(me_dict)

# Instead of calling 'name' and 'hair' the index, we call them keys. 
# Each key is associated with a value in a key-value pair.
# We can see the key-value pairs in the {} syntax used for creating a dict. 
# Each key-value pair is separated by a comma,
# and within a pair the key and value are separated by a colon :

print('My name is %s' % me_dict['name'])
print('I have %s hair' % me_dict['hair'])