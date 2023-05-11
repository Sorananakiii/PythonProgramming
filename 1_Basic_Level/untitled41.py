
# Global Variables
### Defining inside versus outside a Function
# When you define a variable at the start of a script, it will be a global variable, accessible from anywhere in the script. 
# This includes within the functions themselves

x = 5
def do_things():
    print(x)
do_things()

# However, if you define a variable within a function, it is only accessible within that function
def my_func():
    k = 5
    return 2

my_func()
print(k)