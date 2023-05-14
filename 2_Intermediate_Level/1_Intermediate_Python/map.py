import math

# mapping with Lambda Functions
simpsons = ['homer', 'marge', 'bart']

# find len for each word in list
print([len(word) for word in simpsons])
print([*map(len, simpsons)])
print([word[-1] for word in simpsons])
print([*map(lambda word: word[-1], simpsons)])

nums = [-3, -5, 1, 4]
list(map(lambda x: 1 / (1 + math.exp(-x)), nums))