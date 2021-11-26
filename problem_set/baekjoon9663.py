q2 = dict()
count = 0

def checkQueen(x):
    global count, q2, num

    if (x == num):
        count += 1
        return

    for i in range(num):
        flag = True
        for j in range(x):
            if (i == q2[j] or abs(j - x) == abs(i - q2[j])):
                flag = False
                break

        if (flag):
            q2[x] = i
            checkQueen(x + 1)


num = int(input())

checkQueen(0)

print(count)