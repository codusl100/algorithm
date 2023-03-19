# 230114
# 백준 10610번

# 30 배수
# 30
# 60
# 90
# 120
# 150
# 180
# 210
# 240
# 270
# 300
# 330
# ... => 백의 자리수, 십의 자리수 고려

# 우선 입력받을 정수를 하나씩 받아서 저장하자

N = input()
arr = list(N)
int_arr = map(int, arr)

# 리스트에 값을 하나씩 저장하고, 이 값들을 조합하려고 했으나 시간 초과
    # 리스트에 값을 하나씩 저장하고, 이 값들을 조합하기
        # if '0' not in arr :
        #     final = -1
        # else :
        #     arr.sort(reverse=True)
        #     while int("".join(arr)) % 30 != 0 : # 30 배수가 아니라면
        #         for i in range(2, len(arr)): # 3 
        #             for j in range(1, i): # 
        #                 arr.sort() 
        #                 arr[i], arr[j] = arr[j], arr[i]
        #                 arr.sort(reverse=True)
        #     final = "".join(arr)
        # print(final)
        
# 분명 빠르게 값을 도출할 수 있는 방법이 있다고 생각했기에 계속 생각한 결과, 3의 배수의 특징을 떠올림
# 3의 배수 특징 : 각 자리수의 합을 더하면 3의 배수!
# 그러면 조건식에서 각 자리수 합 더했을 때 3의 배수가 아니면 -1 return하도록 하자

if '0' not in arr :
    print(-1)
else :
    if sum(int_arr) % 3 == 0:
        arr.sort(reverse=True)
        print("".join(arr))
    else:
        print(-1)
    