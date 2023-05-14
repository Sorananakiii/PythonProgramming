# list operation : reverse
# return reverse element by index

my_lists = ['apple', 'banana', 'pineapple', 'orange', 'bomb']
print(my_lists)
print(my_lists[::-1])  # does not modify the original list
my_lists.reverse()     # modifies the original list
print(my_lists)