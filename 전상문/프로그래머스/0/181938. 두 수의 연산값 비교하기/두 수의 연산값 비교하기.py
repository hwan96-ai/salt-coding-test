def solution(a, b):
    plus = int(f"{a}{b}")
    multiple = 2*a*b
    return plus if plus-multiple >= 0 else multiple