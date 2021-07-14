# 동적계획법: N으로 표현

def solution(N, number):
    anslist = []
    return findAns(N, number, anslist, 1)

def findAns(N, number, anslist, step):
    temp_anslist = []

    if (step > 8):
        return -1

    if (len(anslist) != 0):
        for idx, ans in enumerate(anslist):
            for op in ["", "+", "-", "*", "//", ")*", ")//"]:
                num = ans + op + str(N)
                if (op == ")*" or op == ")//"):
                    num = "(" + num
                temp_anslist.append(num)

                if (eval(num) == number):
                    print(num)
                    return step
    else :
        temp_anslist.append(str(N))
        if (N == number):
            return step

    return findAns(N, number, temp_anslist, step + 1)

if __name__ == '__main__':
    print(solution(5, 12))