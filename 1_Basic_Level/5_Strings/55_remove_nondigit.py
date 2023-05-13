# remove non-digit component
def remove_non_digit(s):
    t = ""
    for c in s:
        if c.isdigit():
            t += c
            # t = t + c
    return t

card_id = "(068)345-6789"
print(remove_non_digit(card_id))