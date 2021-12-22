import sys
from collections import defaultdict

n = int(sys.stdin.readline())
d = defaultdict(int)

for i in list(map(int, (sys.stdin.readline()[:-1]).split(" "))):
    d[i] += 1

m = int(sys.stdin.readline())

for i in list(map(int, (sys.stdin.readline()[:-1]).split(" "))):
    print(d[i], end=" ")