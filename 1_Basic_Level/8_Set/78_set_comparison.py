# set comparisons

s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8) # the <= operator or the issubset method to check if one set is a subset of another
print(s7.issubset(s8))

#  the >= operator or the issuperset method to check whether one set is the superset of another
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)