n = int(input())
l = list()

for i in range(n):
    l.append(int(input()))

def merge(l1, l2):
    length = len(l1)
    idx = 0

    if (len(l2) == 0):
        return l1

    if (len(l1) == 0):
        return l2

    c = l2.pop(0)
    for i in range(length):
        while True:
            if (l1[idx] > c):
                l1.insert(idx, c)
                if (len(l2) == 0):
                    return l1

                c = l2.pop(0)
                idx += 1
            else :
                break
        idx += 1

    l1.append(c)

    return l1 + l2

def merge_sort(numbers):
    length = len(numbers)

    if (length <= 1):
        return numbers

    mid = length // 2

    l1 = merge_sort(numbers[:mid])
    l2 = merge_sort(numbers[mid:])
    return merge(l1, l2)

for j in merge_sort(l):
    print(j)