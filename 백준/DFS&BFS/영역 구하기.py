from collections import deque
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

result = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    ans = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < M) and (0 <= nx < N) and  graph[ny][nx] == 0 : # 그려지지 않은 직사각형이면
                graph[ny][nx] = 1
                q.append((ny, nx))
                ans += 1 
    return ans

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for a in range(y1, y2):
        for b in range(x1, x2):
            graph[a][b] = 1 # 이미 그려진 직사각형

for i in range(M): # y축
    for j in range(N): # x축
        if graph[i][j] == 0:  
            graph[i][j] += 1 
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:   
    print(i, end=' ')