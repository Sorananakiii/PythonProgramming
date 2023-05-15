def do_stuff_with_number(n):
    print(n)

# try & except module for condiition in exception
def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        # Raised when accessing a non-existing index of a list
        except IndexError:
            do_stuff_with_number(0)

catch_this()