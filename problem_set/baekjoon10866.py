import sys

n = int(sys.stdin.readline())
a = list()

for i in range(n):
    s = sys.stdin.readline()[:-1].split(" ")

    if (s[0] == "push_front"):
        a.insert(0, s[1])
    if (s[0] == "push_back"):
        a.append(s[1])
    if (s[0] == "pop_front"):
        if (len(a) == 0):
            print(-1)
        else :
            print(a.pop(0))
    if (s[0] == "pop_back"):
        if (len(a) == 0):
            print(-1)
        else:
            print(a.pop())
    if (s[0] == "size"):
        print(len(a))
    if (s[0] == "empty"):
        if (len(a) == 0):
            print(1)
        else:
            print(0)
    if (s[0] == "front"):
        if (len(a) == 0):
            print(-1)
        else:
            print(a[0])
    if (s[0] == "back"):
        if (len(a) == 0):
            print(-1)
        else:
            print(a[len(a) - 1])