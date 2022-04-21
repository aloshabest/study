
# with open("C:\\Users\\niisi 2th\\Downloads\\nums.txt", "r") as file:
#     s = ''
#     for line in file:
#         for i in line:
#             if i.isdigit():
#                 s += i
#             else:
#                 s += ' '
#     print(sum(list(map(int, s.split()))))




def make_module(step=1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}

m = make_module()
print(m['inc'](10))
print(m['dec'](15))

print()


def memoized(func):
    memory = {}
    def inner(*args):
        if args not in memory:
            memory[args] = func(*args)
        return memory[args]
    return inner
@memoized
def f(x):
    print("Calculating...")
    return x * 10
print(f(1))
print(f(1))
print(f(1))
print(f(42))
print(f(42))