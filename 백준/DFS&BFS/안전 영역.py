import sys
sys.setrecursionlimit(10**7)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
max_height = max(map(max, graph))

result = 0
ans = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and graph[nx][ny] > height:
            visited[nx][ny] = True
            dfs(nx, ny, height) 
    
for k in range(1, max_height+1):
    visited = [[False]*N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]: 
                result += 1
                visited[i][j] = True
                dfs(i, j, k)
    ans = max(ans, result)

print(ans)