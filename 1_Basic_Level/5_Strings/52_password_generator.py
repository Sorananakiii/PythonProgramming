import random

# password generator
def password_generator(length):
    # s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    # print(s)
    # p = random.sample(s, length)
    # print(p)
    # return "".join(random.sample(s, length))
    return "".join(random.sample(list("ABCDEFGHJKLMNPQRSTUVWXYZ23456789"), length))

for i in range(10):
    print(password_generator(8))