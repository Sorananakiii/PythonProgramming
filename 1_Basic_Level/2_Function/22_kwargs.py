''' 
Usage of **kwargs
**kwargs allows you to pass keyworded variable length of arguments to a function. 
You should use **kwargs if you want to handle named arguments in a function.

'''

def print_todo_args(**kwargs): # **kwargs is fit for input with keyword arguments
    print('I need to:')
    for k, v in kwargs.items():
        if v:
            print('  ' + k)

print_todo_args(watch_tv = True, read=False, eat=True, sleep=True) 