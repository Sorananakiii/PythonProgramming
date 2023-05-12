# Recursive function
# A function is a function that calls itself during its execution. 
# This enables the function to repeat itself several times, outputting the result and the end of each iteration.

def factorial_recur (k):
    if k == 1 or k == 0:
        return 1
    return factorial_recur(k-1) * k

a = 5    
print('factorial of ', a ,' is ',factorial_recur(a))