from collections import deque
M, N = map(int, input().split()) # 가로, 세로
graph = [list(map(int, input().split())) for i in range(N)]
visited = [[0]*M for i in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

queue = deque([])
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans - 1)