my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

m = [*my_tuple, *my_list, *my_set]
print(m)





dict_a = {"a":1, "b":2}
dict_b = {"c":3, "d":4}

dict_c = {**dict_a, **dict_b}
print(dict_c)