import sys

n = int(sys.stdin.readline())

a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))

s = 0

for i in range(n):
    a_idx = a_list.index(min(a_list))
    b_idx = b_list.index(max(b_list))

    s += a_list[a_idx] * b_list[b_idx]
    a_list.pop(a_idx)
    b_list.pop(b_idx)

print(s)