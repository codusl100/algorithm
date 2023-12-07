N, K = map(int, input().split())
dp = [0] * (K+1)
dp[0] = 1
arr = []
for i in range(N): 
    arr.append(int(input()))

for coin in arr:
    for i in range(K+1):
        if i - coin >= 0:
            dp[i] = dp[i] + dp[i - coin]

print(dp[K])