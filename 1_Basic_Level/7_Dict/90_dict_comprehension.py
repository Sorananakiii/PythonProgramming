
fruits = ['apple', 'banana', 'cherry']

fruit_lengths = {fruit:len(fruit) for fruit in fruits}
fruit_lengths

# or
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)}
fruit_indices