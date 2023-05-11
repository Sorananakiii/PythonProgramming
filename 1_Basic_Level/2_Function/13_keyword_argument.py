''' 
Keyword arguments

Keyword arguments, also known as named arguments, are optional inputs to functions. 
These arguments have a default value that is taken when the function is called without the keyword argument specified.

'''

def add_suffix(suffix='.com'):
    return 'google' + suffix

print(add_suffix()) # no need input
print(add_suffix('.co.th')) # But can assign it to function