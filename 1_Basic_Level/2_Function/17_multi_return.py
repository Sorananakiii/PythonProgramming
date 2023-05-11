
# multi valuable returns function

def price_with_vat(a):
    vat = a * 7/100
    price = a - vat
    return price , vat # returns tuple

print(price_with_vat(2000))