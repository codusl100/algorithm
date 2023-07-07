N = int(input())
interval = list(map(int, input().split())) # 도로 간 길이
price = list(map(int, input().split()))

result = []
total = 0 

c_price = price[0]

for i in range(len(interval)) :
    if c_price > price[i] :
        c_price = price[i]
    total += c_price * interval[i]
print(total)