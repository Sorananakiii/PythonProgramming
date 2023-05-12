# **kwargs argument
# **kwargs allows you to pass keyworded variable length of arguments to a function. 
# You should use **kwargs if you want to handle named arguments in a function.

# **kwargs is fit for input with keyword arguments
def print_todo_args(**kwargs):
    print('I need to:')
    for k, v in kwargs.items():
        if v:
            print('  ' + k)

print_todo_args(watch_tv = True, read=False, eat=True, sleep=True) 