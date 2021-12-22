import sys

n, k = list(map(int, (sys.stdin.readline()[:-1]).split(" ")))
l = list(range(1, n + 1))
idx = 0

print("<", end="")

while (l):
    idx = (idx + k - 1) % len(l)
    print(l.pop(idx), end="")

    if (len(l) != 0):
        print(", ", end="")

print(">", end="")