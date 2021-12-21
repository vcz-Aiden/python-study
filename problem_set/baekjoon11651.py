import sys
from collections import defaultdict

n = int(sys.stdin.readline())
d = defaultdict(set)
y_list = set()

for i in range(n):
    x, y = list(map(int, (sys.stdin.readline()[:-1]).split(" ")))
    y_list.add(y)
    d[y].add(x)

for y in sorted(y_list):
    for x in sorted(d[y]):
        print(x, y)