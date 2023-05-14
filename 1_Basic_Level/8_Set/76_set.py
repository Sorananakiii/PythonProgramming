# Set

# Python set is also similar to a list, except it is unordered. 
# It can store heterogeneous data and it is mutable,
# but what does it mean to be unordered? The simplest explanation is simply to look at an example.
# We can create a set by enclosing our data with curly brackets {}

example_set = {'Dylan', 26, 167.6, True}
print(example_set)

# print(example_set[0]) will error because unordered

print(example_set.pop()) # cant know which item will be deleted
print(example_set)
print()

example_set.add('True') # similar to list.append
print(example_set)
example_set.update([58.1, 'brown']) # similar to list.extend
print(example_set)

# Set have no index because it unorder.