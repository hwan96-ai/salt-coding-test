def solution(m, n, puddles):
    dp = [[0] * n  for _ in range(m)]

    for x, y in puddles:
        dp[x-1][y-1] = -1

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                continue
            down = dp[i-1][j] if i > 0 else 0
            right = dp[i][j-1] if j > 0 else 0
            dp[i][j] = (down + right) % 1000000007

    return dp[m-1][n-1]