
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


# some of input is keyword arguments and combined it with positional
def print_todo_default(watch_tv, read, eat=True, sleep=True):
    print('I need to:')
    if watch_tv:
        print('  watch_tv')
    if read:
        print('  read')
    if eat:
        print('  eat')
    if sleep:
        print('  sleep')
        
print_todo_default(True, True)


# Another thing we might want to do is take a variable list of arguments, lets write a similar.
# todo function as before, but this time we will allow it to pass in any number of arguments.
# Here we will make use of the *args syntax. This * tells python to gather the rest of the arguments into the tuple args.