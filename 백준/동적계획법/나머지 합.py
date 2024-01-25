n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
dp = [0] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    dp[i] = dp[i-1] + arr[i-1]
    dp[i] = dp[i] % m

ans = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if dp[i] - dp[j] == 0:
            ans += 1

print(ans)