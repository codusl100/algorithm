N, M = map(int, input().split()) # M이 스타트

num = int(input())

left = 1
right = M
count = 0

for i in range(num):
    x = int(input())
    if left <= x and right >= x:
        pass
    elif left > x:
        count += (left - x)
        right -= (left - x)
        left = x
    else :
        count += (x - right)
        left += (x - right)
        right = x
print(count)