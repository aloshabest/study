import sys

for line in sys.stdin:
    line = line.rstrip()

    while True:
        w = []
        q = []
        c = 0
        for i in range(len(line)):
            if line[i] not in w:
                w.append(line[i])
            elif i in w:
                q.append(line[i])
            if (q == w) and (line[i + 1] == ''):
                print(line)
                c = 1
                break
        if (c == 1) or (q != w):
            break