N = int(input())
num_list = list(map(int, input().split()))

for i in range(1, N):
    num_list[i] = max(num_list[i], num_list[i-1] + num_list[i])
print(max(num_list))

10 6 9 10 15 21 -35 12 33