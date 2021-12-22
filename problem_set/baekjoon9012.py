import sys

n = int(sys.stdin.readline())

for i in range(n):
    l = list()
    n_flag = False
    for s in sys.stdin.readline()[:-1]:
        if (s == "("):
            l.append(s)
        elif (s == ")"):
            if (len(l) == 0):
                n_flag = True
                break
            else :
                l.pop()

    if (n_flag):
        print("NO")
        continue

    if (len(l) == 0):
        print("YES")
    else :
        print("NO")