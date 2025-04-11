def solution(triangle):
    n = len(triangle)
    if n == 1:
        return triangle[0][0]

    max_values = [row[:] for row in triangle]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            max_values[i][j] += max(max_values[i + 1][j], max_values[i + 1][j + 1])

    return max_values[0][0]