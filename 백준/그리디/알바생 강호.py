N = int(input())
money = []
for i in range(N):
    money.append(int(input()))

money.sort(reverse=True)
money.insert(0, 0)
total = 0

for i in range(1, N+1):
    plus = money[i] - (i - 1)
    if plus < 0 :
        pass
    else :
        total += plus

print(total)