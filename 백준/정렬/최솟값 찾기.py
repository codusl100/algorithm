from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lists = list(map(int, input().split()))
q = deque()

for i in range(N):
    while q and q[-1][0] > lists[i]:
        q.pop()
    q.append((lists[i], i))
    if q[0][1] <= i - L:
        q.popleft()
    print(q[0][0], end = " ")