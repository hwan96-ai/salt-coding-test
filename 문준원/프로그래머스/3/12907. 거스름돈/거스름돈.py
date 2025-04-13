def solution(n, money):
    cases = [0] * (n + 1)
    cases[0] = 1

    for coin in money:
        for i in range(coin, n + 1):
            cases[i] += cases[i - coin]

    return cases[n] % 1000000007