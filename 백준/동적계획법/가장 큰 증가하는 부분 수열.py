N = int(input())
num_list = list(map(int, input().split()))


dp = [1] * N
dp[0] = num_list[0]

for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+num_list[i])
        else:
            dp[i] = max(dp[i], num_list[i])

print(max(dp))