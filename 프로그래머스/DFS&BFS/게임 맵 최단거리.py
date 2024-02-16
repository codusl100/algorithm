from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(a, b):
        queue = deque([(a, b)])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1 :
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))
        return maps[n-1][m-1]

    if bfs(0,0) == 1:
        return -1
    else:
        return bfs(0,0)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))