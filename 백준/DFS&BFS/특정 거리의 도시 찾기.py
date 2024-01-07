import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
visited[X] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]

def dfs(v):
    q = deque([v])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visited[next_node] == -1: # 아직 방문 전
                visited[next_node] = visited[now] + 1
                q.append(next_node)

dfs(X)

check = False
for i in range(1, N+1):
    if visited[i] == K: # 최단 거리가 K인 경우 뽀바내기
        print(i)
        check = True

if check == False:
    print(-1)