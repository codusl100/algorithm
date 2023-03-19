# 230115
# 백준 13458번

N = input()
A = list(map(int, input().split()))
B, K = map(int, input().split())

count = int(N)
    
for i in range(len(A)):
    A[i] -= B
    while A[i] > 0 :
        if A[i] < K :
            count += 1
            break
        else :
            count += (A[i] // K)
            A[i] %= K
print(count)

# 주감독 외 부감독이 맡게 될 때 경우의 수를 나눠서 case를 나눔
# 첨에 일일이 다 빼려고 했으나 그러는 경우 시간 초과되므로
# 나누기를 이용해서 시간 단축 성공