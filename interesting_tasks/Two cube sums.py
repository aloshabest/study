#Задача Codewars: 6 kyu.
#which checks if a given number n can be written as the sum of two cubes in two different ways: n = a³+b³ = c³+d³.
# All the numbers a, b, c and d should be different and greater than 0.

def has_two_cube_sums(n):
    lst = []
    def sumCube(n):
        s = dict()
        for i in range(n):
            if i ** 3 > n:
                break
            if i not in lst:
                s[i ** 3] = 1
                if (n - i ** 3) in s.keys():
                    lst.append((n - i ** 3) ** (1 / 2))
                    lst.append(i)

    for i in range(2):
        sumCube(n)

    if len(lst) >= 4:
        return True
    else:
        return False
print(has_two_cube_sums(4105))
