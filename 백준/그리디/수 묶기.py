# 230117
# 백준 1744번

# 처음 문제를 보고 든 생각이 
# 그냥 더했을 때가 곱할 때보다 작을 수도 있음
# 같은 경우 안 곱하는게 낫고, 0이 있는 경우 0이랑 곱하기
# 이런 케이스를 나눠서 채점한 결과 틀려서 분명 내가 놓친 조건이 있다고 생각함
# 여러 경우의 수를 대입해본 결과, 음수가 여러개일 때 조건을 빼먹었다!
# 0 포함 양수, 1, 음수 이렇게 리스트를 나눠서 각기 조건별로 정수들을 분류했더니 성공

N = int(input())

plus_list = list()
one_list = list() # 1만 담음
minus_list = list()
for i in range(N) :
    num = int(input())
    if num == 1 :
        one_list.append(num)
    elif num >= 0 :
        plus_list.append(num)
    else :
        minus_list.append(num)

plus_list.sort(reverse=True)
minus_list.sort(reverse=True)

sum_list = list()

# 음수 처리
while True:
    if len(minus_list) >= 2 :
        sum_list.append(minus_list[-1] * minus_list[-2])
        minus_list.remove(minus_list[-1])
        minus_list.remove(minus_list[-1])
    elif len(minus_list) == 1 :
        if 0 in plus_list :
            sum_list.append(minus_list[0] * 0)
            minus_list.remove(minus_list[0])
            plus_list.remove(0)
        else :
            sum_list.append(minus_list[0])
            minus_list.remove(minus_list[0])
    else :
        break
    # 6 5 2 1 0 -3 -5
# 양수 처리   
while True:
    if 0 in plus_list :
        plus_list.remove(0)
    elif len(plus_list) >= 2: 
        sum_list.append(plus_list[0] * plus_list[1])
        plus_list.remove(plus_list[0])
        plus_list.remove(plus_list[0])
    else :
        if len(plus_list) == 0:
            break
        sum_list.append(plus_list[0])
        break
    
for i in range(len(one_list)) :
    sum_list.append(one_list[i])
    
print(sum(sum_list))