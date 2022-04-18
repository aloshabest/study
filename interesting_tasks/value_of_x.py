# Задача Codewars: 5 kyu
# Jack's teacher gave him a ton of equations for homework. The thing is they are all kind of same so they are boring.
#
# So help him by making a equation solving function that will return the value of x.
#
# Test Cases will be like this:
#
# # INPUT            # RETURN
# 'x + 1 = 9 - 2'    # 6
# '- 10 = x'         # -10
# 'x - 2 + 3 = 2'    # 1
# '- x = - 1'        # 1




def solve(eq: str):
    left, right = eq.split(' = ')
    if 'x' in right:
        left, right = right, left
    right = eval(right)
    x = left.find('x')
    pos = x==0 or left[x-2]=='+'
    left = eval(left[:max(0, x-3)]+left[x+2:] or "0")
    return right-left if pos else left-right


print(solve('x - 2 + 3 = 2'))