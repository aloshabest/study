import re

with open("C:\\Users\\niisi 2th\\Downloads\\cyrillic.txt", "r", encoding='UTF-8') as file:

    lst = [line.split() for line in file]

    have = []
    haven_t = []
    for i in range(len(lst)):
        if len(lst[i]) > 0:
            if lst[i][0] == 'def':
                if len(lst[i-1]) > 0 and lst[i-1][0] == '#' and i != 0:
                    s = lst[i][1].split('(')
                    have.append(s[0])
                else:
                    s = lst[i][1].split('(')
                    haven_t.append(s[0])


    print(*haven_t, sep='\n')