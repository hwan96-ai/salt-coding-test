def main():
    print(solution(16, [2, 9], 2))


import math


def solution(n, stations, w):
    answer = 0
    w_range = w * 2 + 1
    start = 0

    for station in stations:
        left = station - w - 1
        if left > start:
            answer += math.ceil((left - start) / w_range)
        start = station + w

    if start < n:
        answer += math.ceil((n - start) / w_range)

    return answer

    # i = 0
    # while i < n:
    #     if apartList[i] == 0:
    #         start = i
    #         while i < n and apartList[i] == 0:
    #             i += 1
    #         end = i - 1
    #         answer += math.ceil((end - start + 1) / (w * 2 + 1))
    #     else:
    #         i += 1
    # return answer


if __name__ == "__main__":
    main()
