# Nested loop
# lopp which have another loop inside
def nest(a, b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            print('%d x %d = %d' %(i, j, i*j))

nest(5, 5)