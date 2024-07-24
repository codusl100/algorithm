n = int(input())
arr = list(map(int, input().split()))
x = int(input())

l = 0
r = n - 1
cnt = 0
arr.sort()
while l < r:
    if arr[l] + arr[r] == x:
        cnt += 1
        l += 1
        r -= 1
    elif arr[l] + arr[r] > x:
        r -= 1
    elif arr[l] + arr[r] < x:
        l += 1
    

print(cnt)