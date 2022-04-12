# Задача Codewars: 5 kyu
#Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer.
#In the case that there are no arguments (or the provided array in compiled languages is empty), return 1.


def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)


def LcmOfArray(arr, idx):
    if (idx == len(arr) - 1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx + 1)
    return int(a * b / __gcd(a, b))


def lcm(*args):
    if len(args) == 0:
        return 1
    elif 0 in args:
        return 0
    else:
        return LcmOfArray(args, 0)

print(lcm(2, 5))
print(lcm(2, 3, 4))
print(lcm(0, 1, 0))