
'''
_**Why is `set` useful?**_

It seems strange that we might want an _unordered_ data structure. We can't access or modify the data through indexing. How does giving up order benefit us? The answer is that it gives us flexibility about how the data is stored in memory, and that flexibility can make data retrieval much faster.

Imagine we have ten boxes and ten piles of money. We put the ten piles of money in the ten boxes. Now say we want to find the box that has \$5.37 in it. We don't know which box this is, so we start with the first box and check. If it isn't in the first box, we move on to the second box. We keep checking boxes until we find it. This might take awhile.

Now imagine we have the same ten piles of money, but we have 31 boxes. Instead of putting each pile of money into the boxes in order, instead put each pile into a box based on the amount of money in the pile. First we multiply the amount of money by 100, and then take modulus division by 31. This gives the number of the box we should put the pile of money in.
'''

s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8) # the <= operator or the issubset method to check if one set is a subset of another
print(s7.issubset(s8))

#  the >= operator or the issuperset method to check whether one set is the superset of another
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)