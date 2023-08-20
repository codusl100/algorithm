import heapq, sys
INF = int(1e9)
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

target1, target2 = map(int, input().split())

def dijkstra(start, end):
    distance = [sys.maxsize]*(N+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist :
            continue
        for nnode, ndist in graph[node]:
            cost = dist + ndist
            if cost < distance[nnode]:
                distance[nnode] = cost
                heapq.heappush(queue, (cost, nnode))
    return distance[end]

path1 = dijkstra(1, target1) + dijkstra(target1, target2) + dijkstra(target2, N)
path2 = dijkstra(1, target2) + dijkstra(target2, target1) + dijkstra(target1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))