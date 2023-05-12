# sometimes our function has too many input
# all of input is postitional arguments
def print_todo(watch_tv, read, eat, sleep):
    print('I need to:')
    if watch_tv:
        print('  watch_tv')
    if read:
        print('  read')
    if eat:
        print('  eat')
    if sleep:
        print('  sleep')
        
print_todo(True, True, True, True)

# *args argument
# *args is fit for input with positional arguments
def print_todo_args(*args):
    print('I need to:')
    for arg in args:
        print('  ' + arg)

print_todo_args('watch_tv', 'read', 'eat', 'sleep')