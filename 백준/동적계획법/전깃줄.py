N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
arr.sort(key=lambda x: x[0])
dp = [1] * N
result = 0
for i in range(1, N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))