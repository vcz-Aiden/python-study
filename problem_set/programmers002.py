# 동적 계획법: 정수 삼각형

def solution(triangle):
    for i in range(1, len(triangle)):
        for idx, num in enumerate(triangle[i]):
            if (idx == 0):
                triangle[i][idx] += triangle[i - 1][0]
            elif (idx == len(triangle[i]) - 1):
                triangle[i][idx] += triangle[i - 1][-1]
            else :
                triangle[i][idx] += max(triangle[i - 1][idx - 1], triangle[i - 1][idx])

    return max(triangle[-1])

if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))