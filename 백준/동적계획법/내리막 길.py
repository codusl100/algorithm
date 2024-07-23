M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

def recur(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    route = 0
    for i in range(4):
        ey = y + dy[i]
        ex = x + dx[i]
        if 0 <= ey < M and 0 <= ex < N:
            if graph[y][x] > graph[ey][ex]:
                route += recur(ey, ex)
    dp[y][x] = route
    return dp[y][x]
answer = recur(0, 0)
print(answer)