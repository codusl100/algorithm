n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
cnt = 0
sum = arr[0]

while True :
    if sum == m:
        cnt += 1
        sum -= arr[left]
        left += 1
    elif sum < m:
        if right < n:
            sum += arr[right]
            right += 1
        else:
            break
    else:
        sum -= arr[left]
        left += 1

print(cnt)