''' 
*args and **kwargs 

... Are mostly used in function definitions. 
*args and **kwargs allow you to pass a variable number of arguments to a function. 
What does variable mean here is that you don't know before hand that how many arguments can be passed to your function 
by the user so in this case you use these two keywords. 

*args is used to send a non-keyworded variable length argument list to the function.

'''

def print_todo_args(*args): # *args is fit for input with positional arguments
    print('I need to:')
    for arg in args:
        print('  ' + arg)

print_todo_args('watch_tv', 'read', 'eat', 'sleep')