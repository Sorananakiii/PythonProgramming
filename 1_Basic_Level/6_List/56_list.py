# List
# one of 4 basic data structure in python
# List is a sequence of values. In a string, the values are characters; in a list, 
# they can be any type. The values in list are called elements or sometimes items.

list_items = ['chicken', 'onions', 'rice', 'peppers', 'bananas']

def buy_groceries_list(list_items):
    for item in list_items:
        print('Buying {}...'.format(item))
        
print('List type print : ')
buy_groceries_list(list_items)

# pros : if we make a list as an input
# - reduce number of input argument
# - none fix number of input