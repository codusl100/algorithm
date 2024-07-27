import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def _find(X):
    if par[X] != X:
        par[X] = _find(par[X])
    return par[X]

def _union(A, B): # 최대 높이를 확인해서 합쳐준다! 효과적으로!
    A = _find(A)
    B = _find(B)

    if A < B:
        par[B] = A
    else:
        par[A] = B

N, M = map(int, input().split())

par = [i for i in range(N+1)]

for _ in range(M):
    X, A, B = map(int, input().split())

    if X == 0:
        _union(A, B)
    else:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")