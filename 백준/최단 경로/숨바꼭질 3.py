import heapq, sys
INF = int(1e9)
input = sys.stdin.readline

N, K = map(int, input().split())
distance = [INF]*100001

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist :
            continue
        for nnode, ndist in [(2*node, dist), (node+1, dist+1), (node-1, dist+1)]:
            if 0 <= nnode <= 100000 and ndist < distance[nnode]:
                distance[nnode] = ndist
                heapq.heappush(queue, (ndist, nnode))
                
dijkstra(N)
print(distance[K])