from collections import deque

N, M = map(int, input().split())
maze = [[int(num) for num in input()] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

def bfs(a, b):
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))

bfs(0, 0)

print(maze[N-1][M-1])

