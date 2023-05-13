# string format 

fname = 'sora'
lname = 'payatsuporn'
age = 24

print(fname,lname,age)
print('{} {} age: {}'.format(fname,lname,age))
print('{0} {1} age: {2}'.format(fname,lname,age)) # format index start at 0
print('{1} {0} age: {2}'.format(fname,lname,age))
print()
print('-'*40)

n=12313212132
print('{}'.format(n))
print('{:,}'.format(n))

d=1231.14782312
a=1250.5463
print('{}'.format(d))
print('{:.3f}'.format(d))
print('{:.3f}'.format(a))
print('{:,.3f}'.format(d))
print('{:,.3f}'.format(a))
print('-'*20)
print('{:10,.3f}'.format(d))
print('{:10,.3f}'.format(a))
x=-3434.78281
print('{:20,.3f}'.format(x))
