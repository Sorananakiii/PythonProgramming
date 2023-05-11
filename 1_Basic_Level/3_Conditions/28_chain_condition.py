
# Chained conditionals
'''
    Sometimes there are more than two possibilities and we need more than two
    branches. One way to express a computation like that is a chained conditional
    
    elif is an abbreviation of “else if.” Again, exactly one branch will be executed
    
'''

choice = 'a'
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')