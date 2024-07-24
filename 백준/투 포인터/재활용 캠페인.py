N, X = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = N - 1

remain = 0
cnt = 0

while left <= right:
    if arr[right] == X:
        cnt += 1
        right -= 1
        continue
    if left == right:
        remain += 1
        break
    if arr[left] + arr[right] >= X/2:
        cnt += 1
        left += 1
        right -= 1
    else:
        left += 1
        remain += 1
print(cnt + remain // 3)