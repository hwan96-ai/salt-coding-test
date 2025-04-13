def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    def calculate_max(arr):
        n = len(arr)
        max_values = [0] * n
        max_values[:2] = arr[:2] if n == 1 else [arr[0], max(arr[0], arr[1])]
        for i in range(2, n):
            max_values[i] = max(max_values[i - 1], max_values[i - 2] + arr[i])
        return max_values[-1]

    case1 = calculate_max(sticker[:-1])
    case2 = calculate_max(sticker[1:])

    return max(case1, case2)