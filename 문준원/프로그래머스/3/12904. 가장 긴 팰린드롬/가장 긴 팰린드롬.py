def solution(s):
    answer = 1

    n = len(s)
    for i in range(n):
        for j in range(i + answer, n):
            text = s[i:j+1]
            if text == text[::-1]:
                answer = max(answer, j - i + 1)

    return answer

# [코드 개선]
# 1. 기존 코드의 시간 복잡도는 O(n^3), 개선된 코드는 O(n^2)로 최적화.
# 2. 중복 연산을 방지하기 위해 DP를 사용하여 효율성 향상.
def solution2(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    answer = 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    answer = max(answer, length)

    return answer
