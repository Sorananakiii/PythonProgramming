
def if_else_example(x):
    if x < 50:
        if x % 2 == 0:
            return 'branch a'
        else:
            return 'branch b'
    else:
        return 'branch c'

print(if_else_example(42))
print(if_else_example(51))
print(if_else_example(37))