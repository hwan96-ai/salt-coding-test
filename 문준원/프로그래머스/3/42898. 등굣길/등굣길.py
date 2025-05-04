def solution(m, n, puddles):
    cases = [[0] * m for _ in range(n)]
    cases[0][0] = 1

    for x, y in puddles:
        cases[y - 1][x - 1] = -1

    for i in range(n):
        for j in range(m):
            if cases[i][j] == -1:
                cases[i][j] = 0
                continue
            if i > 0:
                cases[i][j] += cases[i - 1][j]
            if j > 0:
                cases[i][j] += cases[i][j - 1]

    return cases[n - 1][m - 1] % 1000000007