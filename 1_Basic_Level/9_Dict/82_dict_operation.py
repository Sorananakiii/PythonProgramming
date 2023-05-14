# dict operations

me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

# We can replace or delete key-value pairs from the dict
me_dict['nieces/nephews'] = 4
print(me_dict)
del me_dict['favorite book']
print(me_dict)

# pop input key and output value
print(me_dict.pop('siblings'))
print(me_dict)
