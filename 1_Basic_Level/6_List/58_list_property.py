# List is heterogeneous and mutable.
# Heterogeneous type of data because it can hold a collection of mixed objects and a list is heterogeneous.
# Mutable is that, can modify component in list.

int_list = [2, 6, 3049, 18, 37]
float_list = [3.7, 8.2, 178.245, 63.1]
mixed_list = [26, False, 'some words', 1.264]

print(int_list)
print(float_list)
print(mixed_list)

# and We can even put a list inside of a list
list_of_lists = [['a', 'list', 'of', 'words'], [1, 5, 209], [True, True, False]]
print(list_of_lists)

# There are very few restrictions on how we structure a list or what we put in it. 
# This can lead to a very complicated nested structure.
confusing_list = [[23, 73, 50], 'some words', 12.308, [[False, True], 'more words']]
print(confusing_list)
