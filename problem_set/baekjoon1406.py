import sys

l, r = list(sys.stdin.readline()[:-1]), list()
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline()[:-1].split(" ")

    if (s[0] == "L"):
        if (len(l) != 0):
            r.append(l.pop())
    elif (s[0] == "D"):
        if (len(r) != 0):
            l.append(r.pop())
    elif (s[0] == "B"):
        if (len(l) != 0):
            l.pop()
    elif (s[0] == "P"):
        l.append(s[1])

print("".join(l + list(reversed(r))))