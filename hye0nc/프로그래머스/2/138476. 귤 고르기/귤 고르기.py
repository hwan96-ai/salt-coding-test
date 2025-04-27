from collections import Counter

def solution(k, tangerine):

    counter = Counter(tangerine)
    
    sorted_freq = sorted(counter.values(), reverse=True)
    
    count = 0
    for freq in sorted_freq:
        k -= freq
        count += 1
        if k <= 0:
            break
    return count