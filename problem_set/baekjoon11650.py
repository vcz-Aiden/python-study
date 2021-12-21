import sys
from collections import defaultdict

n = int(sys.stdin.readline())
d = defaultdict(set)
x_list = set()

for i in range(n):
    x, y = list(map(int, (sys.stdin.readline()[:-1]).split(" ")))
    x_list.add(x)
    d[x].add(y)

for x in sorted(x_list):
    for y in sorted(d[x]):
        print(x, y)