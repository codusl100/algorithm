import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(N)] # 초기 맵 리스트
temp = [[0] * M for _ in range(N)] # 벽을 설치한 뒤의 맵 리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]
        for i in range(N):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)
        