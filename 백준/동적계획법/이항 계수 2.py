# N, K = map(int, input().split())

# res = 1

# for i in range(K):
#     res = res * (N-1)
# for i in range(1, K+1):
#     res = res // i

# print(res)

import sys
N, K = map(int, sys.stdin.readline().split())
dp=[[1]*(N+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j] # 파스칼 삼각형

print(dp[N][K]%10007)