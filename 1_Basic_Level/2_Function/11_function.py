'''
What is function ? : react user input to generate output
    function have 3 parts
    1. definition name : define name and input of function by using the '' def '' keyword.
    2. Body : Use ' : ' in the end of first line of function to begin write body of function.
        Not every function will have a return statement, but many will.
    3. Output : return variable or maybe not

'''

# A return statement ends a function.
def square(number):
    return number**2

print(square(5.5))


# use variables as function input
my_number = 6
print(square(my_number))