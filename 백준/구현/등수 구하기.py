import sys
input = sys.stdin.readline
N, taesoo, P = map(int, input().split())

if N == 0:
    print(1)
else: 
    score = list(map(int, input().split()))
    if N == P and score[-1] >= taesoo:
        print(-1)
    else:
        rank = N + 1
        for i in range(N):
            if score[i] <= taesoo:
                rank = i + 1
                break
        print(rank)