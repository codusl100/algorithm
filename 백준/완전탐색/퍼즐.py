from collections import deque
target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
arr = [[0] for i in range(3)]
visited = [[0]*3 for i in range(3)]
a = 0
b = 0
ans = 0

for i in range(3):
    x, y, z = map(int, input().split())
    arr[i] = [x, y, z]
    if x == 0:
        a = i
        b = 0
    elif y == 0:
        a = i
        b = 1
    elif z == 0:
        a = i
        b = 2
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited[a][b] = 1
for i in range(3):
    for j in range(3):
        if target[i][j] == arr[i][j]:
            visited[i][j] = 1

def bfs(x, y):
    global ans
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if sum(sum(visited, [])) == 9 and arr[2][2] == 0:
                return ans
            if (0 <= nx < 3) and (0 <= ny < 3) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                ans += 1
                bfs(nx, ny)
    return -1

print(bfs(a, b))
