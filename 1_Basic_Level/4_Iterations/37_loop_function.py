# Build a factorial function
def factorial(a):
    fac = 1
    for i in range(1,a+1):
        fac = fac * i
    return fac
a=5
print('Factorial of ',a, 'is', factorial(a))
print('-'*20)

# calculate permutation and combination
def per(n,r):
    return int(factorial(n)/(factorial(n-r) * factorial(r)))

def combi(n,r):
    return int(factorial(n)/factorial(n-r))

print(per(5,3))
print(combi(5,3))
