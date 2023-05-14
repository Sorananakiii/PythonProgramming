# dict comprehension
me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown'}

me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)

square_lut = {x: x**2 for x in range(10)}
print(square_lut)