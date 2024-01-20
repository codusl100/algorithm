import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 1
    queue = deque([(x, y, 0)])
    while queue:
        x, y, c = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # visited[][][벽을 부순 횟수] = 총 이동 횟수
            if 0 <= nx < N and 0 <= ny < M :
                if map[nx][ny] == 1 and c == 0 and not visited[nx][ny][1]: # 벽을 만났지만 한번도 벽 부순 적 없는 경우
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
                elif map[nx][ny] == 0 and not visited[nx][ny][c]: # 벽 부순 횟수와 상관없이 벽을 안만난 경우
                    queue.append((nx, ny, c))
                    visited[nx][ny][c] = visited[x][y][c] + 1
    return 0

result = bfs(0, 0)

if result:
    print(result)
else:
    print(-1)