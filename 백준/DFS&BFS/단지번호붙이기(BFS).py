from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    N = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # 탐색 중인 위치를 0으로 바꿔 다시 방문하지 않도록 함
    count = 1

    while queue:
        x, y = queue.popleft() # 큐에 들어갔던 좌표 x,y 값을 빼줌
        for i in range(4): # 각 좌표마다 위 아래 왼쪽 오른쪽 이동
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표 이동했는데 그래프 범위 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1: # 만약 1이라면 (= 집 방문 X)
                graph[nx][ny] = 0 # 방문한 곳은 0으로 만든다
                queue.append((nx, ny)) # 새로운 x, y 좌표를 큐에 추가
                count += 1 # count값 1 증가
                # 연이어서 아래서 for문 돌렸을 때 방금 추가한 x, y 좌표를 큐에서 찾아 계속 돈다
    return count

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])