#동적 계획법: 도둑질

def solution(money):
    h1 = [0] * len(money)
    h2 = [0] * len(money)
    h1[0] = money[0]
    h1[1] = max(h1[0], money[1])
    h2[0] = 0
    h2[1] = money[1]

    for i in range(2, len(money) - 1):
        h1[i] = max(h1[i-2] + money[i], h1[i-1])

    for i in range(2, len(money)):
        h2[i] = max(h2[i-2] + money[i], h2[i-1])

    return max(h1[-2], h2[-1])

if __name__ == '__main__':
    print(solution([1, 2, 3, 1]))

    h1 = [0] * 5
    print(h1)