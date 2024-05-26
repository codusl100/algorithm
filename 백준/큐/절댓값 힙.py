import sys, heapq
n = int(sys.stdin.readline())
q = []
for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(k), k))