N = int(input())
dp = list()

for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))