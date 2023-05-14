## Type change
example_list = ['a', 'b', 23, 10, True, 'a', 10]
me_dict = {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown'}

example_tuple = tuple(example_list)
example_set = set(example_tuple)
example_list = list(example_set)

print(example_tuple)
print(example_set)
print(example_list) # note we lost the duplicates because of set

print(sorted(map(str, example_tuple)))
print(sorted(map(str, example_set)))
print(sorted(me_dict.items()))
print(sorted(me_dict))