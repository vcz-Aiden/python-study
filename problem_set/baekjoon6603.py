import sys

def getCase(l1, l2):
    if (len(l2) == 6):
        for k in l2:
            print(k, end=" ")
        print()
        return

    for idx, i in enumerate(l1):
        getCase(l1[idx + 1:], l2 + [i])

while (True):
    s = sys.stdin.readline()[:-1].split(" ")

    if (s[0] == "0"):
        break

    n = int(s[0])
    l = list(map(int, s[1:]))

    getCase(l, [])

    print()

