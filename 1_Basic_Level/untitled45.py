
# Sorting with Lambda Functions
# Another useful function that lambdas are often used with is sorted. This function takes an iterable, such as a list, and sorts them according to a function.

# For example, suppose that you had a list of names, and wanted them sorted by length:

names = ['Ming', 'Jennifer', 'Andrew', 'Boris']
sorted(names, key=lambda x : len(x))