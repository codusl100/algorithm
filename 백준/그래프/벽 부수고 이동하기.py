import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M] * N
wall = [] # 부술 후보
road = []
result = 1000*1000+1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global result, road
    if x == N - 1 and y == M - 1:
        result = min(result, len(road))
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M :
            if map[nx][ny] == 0 and (nx, ny) not in road:
                road.append((nx, ny))
                bfs(nx, ny)
                road.pop()

for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            wall.append((i, j))
bfs(0, 0)
for i in wall:
    map[i[0]][i[1]] = 0
    bfs(0, 0)
    map[i[0]][i[1]] = 1

if result == 1000001:
    print(-1)
else:
    print(result+1)