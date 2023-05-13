# replace function
def replace_demo():
    s = "password"
    s2 = s.replace("a", "@")
    s3 = s.replace("a", "@").replace("o", "0")
    s4 = s.replace("pass", "fail")
    print(s, s2, s3, s4)

replace_demo()