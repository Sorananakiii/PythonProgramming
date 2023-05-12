# Multi argument
# Combined Positional and Keyword argument

def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

print(convert_usd_to_aud(100))
print(convert_usd_to_aud(100, rate=20))

# another example
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z == None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))