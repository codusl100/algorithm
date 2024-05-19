import heapq
n = int(input())
q = []
for i in range(n):
    k = int(input())
    if k == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(k), k))