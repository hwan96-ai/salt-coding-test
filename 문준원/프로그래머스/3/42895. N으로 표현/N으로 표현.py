def solution(N, number):
    if N == number:
        return 1

    cases = [set() for _ in range(9)]
    for i in range(1, 9):
        cases[i].add(int(str(N) * i))
        for j in range(1, i):
            for case in cases[j]:
                for prev_level_case in cases[i - j]:
                    cases[i].add(case + prev_level_case)
                    cases[i].add(case * prev_level_case)
                    if case - prev_level_case > 0:
                        cases[i].add(case - prev_level_case)
                    if prev_level_case != 0:
                        cases[i].add(case // prev_level_case)
        if number in cases[i]:
            return i

    return -1