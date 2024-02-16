N = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, plus, minus, mul, div
    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, now + arr[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - arr[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / arr[i]))
            div += 1

dfs(1, arr[0])

print(max_value)
print(min_value)