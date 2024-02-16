n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
C = [0] * m
ans = 0

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

for i in range(n):
    remainder = dp[i] % m
    if remainder == 0:
        ans += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        ans += (C[i] * (C[i] - 1) // 2) # combination
print(ans)