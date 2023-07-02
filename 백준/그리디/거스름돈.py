money = int(input())

ans = 0;

x = money // 5
left = money % 5
# 거스름돈이 5원보다 작을 때
if money == 0 or money == 1 or money == 3:
    ans = -1
# 나머지 짝수
elif left == 0 :
    ans = x
elif left % 2 == 0:
    ans = x + (left // 2)
# 홀수 
else :
    while left % 2 != 0:
        x -= 1
        left += 5
    ans = x + (left // 2)
print(ans)