import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    f_list = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    if (n == 0):
        sys.stdin.readline()
        queue = deque([])
    else :
        queue = deque(list(map(int, (sys.stdin.readline()[1:-2]).split(","))))
    is_left = True
    error_flag = False

    for f in f_list:
        if (f == "R"):
            is_left = not is_left
        elif (f == "D"):
            if (len(queue) == 0):
                error_flag = True
                print("error")
                break

            if (is_left):
                queue.popleft()
            else :
                queue.pop()

    if (not error_flag):
        print('[', end="")

        s = ""
        while(queue):
            if (is_left):
                s += str(queue.popleft()) + ","
            else :
                s += str(queue.pop()) + ","

        print(s[:-1], end="")

        print(']')