def is_continuius_sequence(lst):
    if len(lst) < 2:
        return False
    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] != 1:
            return False
    return True

print(is_continuius_sequence([10, 11, 12, 13]))
print(is_continuius_sequence([1, 12, 1, 3]))
print(is_continuius_sequence([10, 11, 12, 14]))
print(is_continuius_sequence([]))
print(is_continuius_sequence([6]))
print()



def find_longest_lenght(strs):
    lst = []
    count = 0
    for i in range(1, len(strs)):
        if strs[i] != strs[i-1]:
            count += 1
        elif strs[i] == strs[i-1]:
            lst.append(count)
            count = 0
    lst.append(count)
    return max(lst)

print(find_longest_lenght('abcdeef'))
print(find_longest_lenght('jabjcdel'))
print()





def keep_truthful(lst):
    return list(filter(None, lst))

print(keep_truthful([True, False, '', 'foo']))
print()





def partial_apply(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)
    return newfunc

def greet(name, surname):
    return f"Hello, {name} {surname}!"

f = partial_apply(greet, 'Dorian')
print(f('Grey'))
print()







def flip(func):
    return func

def greet(name, surname):
    return f"Hello, {name} {surname}!"

f = flip(greet)
print(f('Cristian', 'Teodor'))












