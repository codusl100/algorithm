def solution(numbers, target):
    n = len(numbers)
    ans = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal ans
                ans += 1
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0, 0)
    return ans