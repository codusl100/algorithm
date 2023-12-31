def solution(n):
    n_list = list(map(int, str(n)))
    ans = []
    for i in range(len(n_list), 0, -1):
        ans.append(i)
    return ans

print(solution(12345))