def solution(numbers, target):
    def dfs(index, current_sum, history):
        if index == len(numbers):
            return 1 if current_sum == target else 0

        if (index, current_sum) in history:
            return history[(index, current_sum)]

        add_case = dfs(index + 1, current_sum + numbers[index], history)
        subtract_case = dfs(index + 1, current_sum - numbers[index], history)
        history[(index, current_sum)] = add_case + subtract_case

        return history[(index, current_sum)]

    return dfs(0, 0, {})