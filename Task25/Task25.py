import math

def get_digits(digits):
    listtuple = list()

    while digits > 0:
        listtuple.append(digits % 10)
        digits = digits // 10

    listtuple = listtuple[::-1]
    mytuple = tuple(listtuple)
    return mytuple

print(get_digits(123456))
