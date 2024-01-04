N, K = map(int, input().split())
dp = [0] * N
dp[K] = 1
k = 1
print(dp)

for i in range(K+1, N):
    print("i:" + str(i))
    dp[i] = dp[i-1] + k
    k += 1
    print(dp)

print(dp[N-1] % 1000000000)