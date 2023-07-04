def func1(a, b, c):
    print(a, b, c)
    
func1(1, 2, 3)
func1(a=1, b=2, c=3)




def func2(a, b, c, d=4):
    print(a, b, c, d)
    
func2(1, 2, 3, 7)
func2(a=1, b=2, c=3, d=7)




def func3(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
func3(1, 2, 3, 4, 5, 6, 7)
func3(1, 2, 3, 4, 5, 6, seven=7, eight=8)




def foo(a, b, c):
    print(a, b, c)
    
my_list = [0, 1, 2]
foo(*my_list)