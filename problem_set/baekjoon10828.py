import sys

n = int(sys.stdin.readline())
l = list()

for i in range(n):
    s = (sys.stdin.readline()[:-1]).split(" ")

    if (s[0] == "push"):
        l.append(s[1])
    elif (s[0] == "pop"):
        if (len(l) == 0):
            print("-1")
        else:
            print(l.pop())
    elif(s[0] == "size"):
        print(len(l))
    elif(s[0] == "empty"):
        if (len(l) == 0):
            print("1")
        else :
            print("0")
    elif(s[0] == "top"):
        if (len(l) == 0):
            print("-1")
        else:
            print(l[len(l) - 1])