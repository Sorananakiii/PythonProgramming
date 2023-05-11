''' 
Comprehensions are very useful for doing simple transformations on data structures. 
For example, maybe we are writing a function that will analyze me_dict. 
It might be useful to have a dict of the data types of the values in me_dict so that we know what to expect as input.

'''

me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)

square_lut = {x: x**2 for x in range(10)}
print(square_lut)