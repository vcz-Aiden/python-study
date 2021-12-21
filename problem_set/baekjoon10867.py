import sys

n = int(sys.stdin.readline())

i_list = set(map(int, (sys.stdin.readline()[:-1]).split(" ")))

for i in sorted(i_list):
    print(i, end=" ")