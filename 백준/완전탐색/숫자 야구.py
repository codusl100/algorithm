from itertools import permutations

n = int(input())

num = list(range(1, 10))
num_pool = []

for i in permutations(num, 3):
    num_pool.append(i)

queries = []
for _ in range(n):
    number, strike, ball = map(int, input().split())
    queries.append((number, strike, ball))

for number, strike, ball in queries:
    ans = []
    for x in num_pool:
        s, b = 0, 0
        number_str = str(number)
        for i in range(3):
            if int(number_str[i]) == x[i]:
                s += 1
            elif int(number_str[i]) in x:
                b += 1
        if s == strike and b == ball:
            ans.append(x)
    num_pool = ans

print(len(num_pool))