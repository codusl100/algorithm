n = int(input())
left = 1
right = 1

sum = 1
result = 1

while right != n:
    if sum == n:
        result += 1
        right += 1
        sum += right
    elif sum > n:
        sum -= left
        left += 1
    elif sum < n:
        right += 1
        sum += right
print(result)