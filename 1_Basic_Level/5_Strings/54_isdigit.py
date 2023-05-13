# isdigit == check which is a numbers and return True
def demo_isdigit(p):
    total = 0
    for c in p:
        # print(c)
        if c.isdigit():
            # print(c)
            total += int(c)
    return total


plate = "ASVS 4567"
print(demo_isdigit(plate))