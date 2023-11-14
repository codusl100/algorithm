import sys
sys.setrecursionlimit(10**7)

N = int(input())

cnt = 0
cnt2 = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def dfs(x, y):
    visited[x][y] = 1
    color = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == 0 and graph[nx][ny] == color:
                dfs(nx, ny)
   
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[0] * N for _ in range(N)] # 방문 초기화

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt2 += 1

print(cnt, cnt2)