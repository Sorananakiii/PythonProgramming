''' 
# Recursive function

When a function calls itself, it is known as a Recursive Function. This is like for loops. 
However, sometimes it allows us to write more elegant and terse functions than can be achieved with a loop.

You can imagine that a function that calls itself might end up in an infinite loop; 
it is true that you can write a recursive function that will keep running indefinitely

Recursive function : A recursive function is a function that calls itself during its execution. 
This enables the function to repeat itself several times, outputting the result and the end of each iteration.
'''
def factorial_recur (k):
    if k==1 or k==0:
        return 1
    return factorial_recur(k-1) * k

a=5    
print('factorial of ', a ,' is ',factorial_recur(a))