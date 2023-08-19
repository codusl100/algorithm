import heapq, sys
INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [sys.maxsize]*(V+1)
ans = 0

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:  
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for nnode, ncost in graph[node]:
            cost = dist + ncost
            if cost < distance[nnode]:
                distance[nnode] = cost
                heapq.heappush(queue, (cost, nnode))

dijkstra(K)

for i in range(1,V+1):
    if distance[i] >= INF:
        print("INF")
    else:
        print(distance[i])