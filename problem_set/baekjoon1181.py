import sys
from collections import defaultdict

n = int(sys.stdin.readline())
d = defaultdict(set)

for i in range(n):
    w = sys.stdin.readline()[:-1]
    d[len(w)].add(w)

for i in range(51):
    for j in sorted(d[i]):
        print(j)