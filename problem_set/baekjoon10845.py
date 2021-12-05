import sys

num = int(sys.stdin.readline())
a = list()

for i in range(num):
    t = sys.stdin.readline()[:-1].split(" ")

    if (t[0] == "push"):
        a.append(t[1])
    elif (t[0] == "pop"):
        if (len(a) == 0) :
            print(-1)
        else :
            print(a.pop(0))
    elif (t[0] == "size"):
        print(len(a))
    elif (t[0] == "empty"):
        if (len(a) == 0):
            print(1)
        else:
            print(0)
    elif (t[0] == "front"):
        if (len(a) == 0):
            print(-1)
        else:
            print(a[0])
    elif (t[0] == "back"):
        if (len(a) == 0):
            print(-1)
        else:
            print(a[len(a) - 1])