
# Nested conditionals
'''
    One conditional can also be nested within another. We could have written the
    three-branch example like this
    
    Although the indentation of the statements makes the structure apparent, nested
    conditionals become difficult to read very quickly. In general, it is a good idea to avoid them when you can
    
'''
x = 2
y = 3

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
        