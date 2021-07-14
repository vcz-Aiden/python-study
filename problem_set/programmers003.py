#동적 계획법: 등굣길
import numpy as np

def solution(m, n, puddles):
    num_list = np.zeros((m, n))
    num_list[0, 0] = 1

    for p in puddles:
        num_list[p[0] - 1][p[1] - 1] = -1

    for i in range(m):
        for j in range(n):
            if (num_list[i][j] == -1 or i == 0 and j == 0):
                continue
            ans = 0
            if (num_list[i - 1][j] != -1 and i - 1 >= 0):
                ans += num_list[i - 1][j]
            if (num_list[i][j - 1] != -1 and j - 1 >= 0):
                ans += num_list[i][j - 1]

            num_list[i][j] = int(ans % 1000000007)

    return int(num_list[m - 1][n - 1] % 1000000007)

if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))