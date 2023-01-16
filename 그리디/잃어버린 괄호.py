# 230116
# 백준 1541번

# 아래처럼 풀었더니 계속 런타임 에러 발생

# str = list(input())
# num = list() # 숫자 합치기 전 담는 리스트
# num_list = list()
# plus_minus = ['+', '-']
# p_m = list()

# i = 0
# while True :
#     if str[i] not in plus_minus and i < len(str): # 숫자라면
#         num.append(str[i])
#     else : # 연산자라면
#         num_list.append(int(''.join(num))) # 합치기 전 리스트 합쳐주고 num_list에 담기
#         num.clear()
#         p_m.append(str[i])
#     i += 1
#     if i == len(str) :
#         break

# num_list.append(int(''.join(num)))

# while True:
#     if '-' not in p_m : # 더하기만 있을 때
#         print(sum(num_list))
#         break
#     elif '+' not in p_m : # 빼기만 있을 때
#         for i in range(len(p_m)):
#             num_list[0] -= num_list[i + 1]
#         print(num_list[0])
#         break
#     else :
#         for i in range(0, len(p_m)-1) :
#             if p_m[i] == '-' and p_m[i + 1] == '+' :
#                 num_list[i + 1] += num_list[i + 2]
#                 num_list.remove(num_list[i + 2])
#                 p_m.remove(p_m[i + 1])
#             elif p_m[i] == '+' and p_m[i + 1] == '-' :
#                 num_list[i] += num_list[i + 1]
#                 num_list.remove(num_list[i + 1])
#                 p_m.remove(p_m[i])


# 입력받는 연산값들을 나누려고 복잡하게 할 필요가 없었음
# 우선 입력받는 값들을 -으로 나누자
str = input().split('-')
sum = 0

for i in str[0].split('+') :
    sum += int(i)
for i in str[1:] : # -으로 나눌 때 뒷부분
    for j in i.split('+') :
        sum -= int(j)
print(sum)

# 문제 조건에서 연속해서 두 개 이상에 연산자가 나올 수 없다는 걸 간과했다
# 즉 + - + - + 이렇게는 안되고 + - - 나 - + + 는 되는 것..
# 그러면 딱 바뀌는 지점의 연산자를 기점으로 해서 그 뒤로 나누고 값을 더하면 되는 것이었다
# 마지막 이중 for문에서 +을 나누는 이유가 -으로는 이미 나뉘어졌고,
# 그 이후에 +가 있다는 것을 고려하여 sum 값에 빼주는 것이다