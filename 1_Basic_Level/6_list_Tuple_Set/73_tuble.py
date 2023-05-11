
# One common mistake people make with immutability and especially with tuples is to assume data structures
# inside the tuple are immutable because the tuple is immutable. Lets see an example.

tup = tuple([[], 'a'])
print(tup)
tup[0].append(1)
print(tup)