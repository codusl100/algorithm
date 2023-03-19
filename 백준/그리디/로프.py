# 230116
# 백준 2217번

N = int(input())
max_weight = list()
max_list = list()

for i in range(N):
    max_weight.append(int(input()))

max_weight.sort()

i = 0

while i < len(max_weight) :
    max_list.append(max_weight[i] * N)
    N -= 1
    i += 1

print(max(max_list))

# 첨에는 
# N = int(input())
# max_weight = list()
# for i in range(N) :
#     max_weight.append(int(input()))

# max_weight.sort()
# result = list()

# while len(max_weight) >= 2:
#     min_num = min(max_weight) 
#     result.append(min_num * len(max_weight))
#     max_weight.remove(min_num)
    
# print(min(result))

# 이렇게 단순히 주어진 로프의 최대 무게 중 젤 작은 거에 N을 곱하면 되겠다했는데
# 문제 조건에서 로프 다 사용 안해도 된다고 한 걸 빼먹었다
# 로프 하나만 사용하지 않을 테니.. 최소 두개라 가정하고 구했더니 풀었다!