def solution(begin, target, words):
    word_size = len(words[0])

    replaceable_patterns_map = {}
    for word in words:
        for i in range(word_size):
            search_keyword = f"{word[0:i]}?{word[i + 1:word_size]}"
            if search_keyword not in replaceable_patterns_map:
                replaceable_patterns_map[search_keyword] = []
            replaceable_patterns_map[search_keyword].append(word)

    visited = [False] * len(words)

    queue = [(begin, 0)]
    while queue:
        current_word, count = queue.pop(0)

        if current_word == target:
            return count

        for i in range(word_size):
            search_keyword = f"{current_word[0:i]}?{current_word[i + 1:word_size]}"
            if search_keyword not in replaceable_patterns_map:
                continue

            replaceable_words = replaceable_patterns_map[search_keyword]
            for replaceable_word in replaceable_words:
                if visited[words.index(replaceable_word)]:
                    continue

                visited[words.index(replaceable_word)] = True
                queue.append((replaceable_word, count + 1))
    return 0