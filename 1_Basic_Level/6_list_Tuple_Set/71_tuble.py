
# Tuble
# A Python `tuple` is very similar to a `list` with one major difference -- it is immutable. 
# We create a `tuple` using parentheses `()`.

t1 = ('a',)
type(t1)

t2 = ('a')
type(t2)

t = tuple('lupins')
print(t)

# Tuble

# A Python tuple is very similar to a list with one major difference -- it is immutable.
# immutable that mean cant modify item in the tuble
# We create a tuple using parentheses ()

example_tuple = ('Dylan', 26, 167.6, True)
print(example_tuple)

# tuble index similar to a list
print(example_tuple[2])

another_example_tuple = 'Jill', 36, 162.3, True
print(another_example_tuple)
print(type(another_example_tuple))

print(example_tuple.count('a'))
print(example_tuple.count(26))

print(example_tuple.index(26))
print(example_tuple.index(167.6))