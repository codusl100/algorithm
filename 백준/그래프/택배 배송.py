import heapq, sys
INF = int(1e9)

N, M = map(int, input().split()) # N = 헛간의 개수
graph = [[] for _ in range(N+1)]
distance = [sys.maxsize]*(N+1)
ans = 0

for _ in range(M):
  a, b, cost = map(int, input().split())
  graph[a].append((cost, b))
  graph[b].append((cost, a))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:  
        cost, node = heapq.heappop(queue) # 가장 최단 거리 노드 정보 꺼내기
        if node == N:
            return distance[node]
        if distance[node] < cost : # 현재 노드 이미 처리되면
            continue
        for ncost, nnode in graph[node]: # 현재 노드와 연결된 다른 인접한 노드 확인
            if cost + ncost < distance[nnode]:
                distance[nnode] = cost + ncost
                heapq.heappush(queue, (cost + ncost, nnode))

print(dijkstra(1))