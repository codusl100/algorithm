# 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램
N, M = map(int, input().split())
rect = [0] * N
for i in range(N):
    rect[i] = list(map(int, input()))
# rect = [list(map(int, list(input())) for _ in range(N))]

ans = 0

# -
# -
# -
for i in range(1, N-1):
    for j in range(i+1, N):
        s1 = sum([rect[a][b] for a in range(i) for b in range(M)])
        s2 = sum([rect[a][b] for a in range(i, j) for b in range(M)])
        s3 = sum([rect[a][b] for a in range(j, N) for b in range(M)])
        ans = max(ans, s1*s2*s3)

# |||
for i in range(1, M-1):
    for j in range(i+1, M):
        s1 = sum([rect[a][b] for a in range(N) for b in range(i)])
        s2 = sum([rect[a][b] for a in range(N) for b in range(i, j)])
        s3 = sum([rect[a][b] for a in range(N) for b in range(j, M)])
        ans = max(ans, s1*s2*s3)

# ㅗ
for i in range(1, M):
    for j in range(1, N):
        s1 = sum([rect[a][b] for a in range(j) for b in range(i)])
        s2 = sum([rect[a][b] for a in range(j) for b in range(i, M)])
        s3 = sum([rect[a][b] for a in range(j, N) for b in range(M)])
        ans = max(ans, s1*s2*s3)

# ㅜ
for i in range(1, N):
    for j in range(1, M):
        s1 = sum([rect[a][b] for a in range(i) for b in range(M)])
        s2 = sum([rect[a][b] for a in range(i, N) for b in range(j)])
        s3 = sum([rect[a][b] for a in range(i, N) for b in range(j, M)])
        ans = max(ans, s1*s2*s3)
    
# ㅓ
for i in range(1, N):
    for j in range(1, M):
        s1 = sum([rect[a][b] for a in range(i) for b in range(j)])
        s2 = sum([rect[a][b] for a in range(i, N) for b in range(j)])
        s3 = sum([rect[a][b] for a in range(N) for b in range(j, M)])
        ans = max(ans, s1*s2*s3)

# ㅏ
for i in range(1, N):
    for j in range(1, M):
        s1 = sum([rect[a][b] for a in range(i) for b in range(j, M)])
        s2 = sum([rect[a][b] for a in range(i, N) for b in range(j, M)])
        s3 = sum([rect[a][b] for a in range(N) for b in range(j)])
        ans = max(ans, s1*s2*s3)

print(ans)