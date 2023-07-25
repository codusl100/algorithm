from collections import deque
T = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(a, b):
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if x == x2 and y == y2 :
                return graph[x2][y2] - 1
            if 0 <= nx < d and 0 <= ny < d and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

for _ in range(T):
    d = int(input())
    graph = [[0 for _ in range(d)] for _ in range(d)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph[x1][y1] = 1
    print(bfs(x1, y1))