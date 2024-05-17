n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for m in range(len(arr)):
    k = arr[m]
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == k:
            if i != m and j != m:
                result += 1
                break
            elif i == m:
                i += 1
            elif j == m:
                j -= 1
        elif arr[i] + arr[j] < k:
            i += 1
        else:
            j -= 1
print(result)