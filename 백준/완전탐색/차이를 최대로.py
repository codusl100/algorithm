from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
p = list(permutations(arr, N))
sum = 0

for p_arr in p:
    print(p_arr)
    temp = 0
    for i in range(N-1):
        temp += abs(p_arr[i] - p_arr[i+1])
    sum = max(sum, temp)

print(sum)