N = int(input())

num_list = list(map(int, input().split()))
num_list = sorted(num_list, reverse=True)

drink = num_list[0]

for i in range(1, N):
    drink += num_list[i] / 2


print(drink)