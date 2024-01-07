import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
car = [0] * 100
for i in range(3):
    in_, out_ = map(int, input().split())
    for j in range(in_, out_):
        car[j] += 1
ans = 0
for i in car:
    if i == 1:
        ans += A * i
    elif i == 2:
        ans += B * i
    elif i == 3:
        ans += C * i
print(ans)