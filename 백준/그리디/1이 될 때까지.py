N, K = map(int, input().split())

x = 0
count = 0

if N % K == 0 : # 바로  나뉠 때
    while(N != 1) :
        count += 1      
        N = N / K  
elif N % K != 0 : # 바로 안 나뉠 때
    x = N % K # 뺄 값들
    count += x
    N = N - x
    while(N != 1) :
        count += 1 
        N = N / K
        
print(count)

result = 0

# 처음 작성한 풀이에서는 안나눠지면 단순하게 배수일 때까지 빼고 구하면 되겠다 했는데,
# N이 K보다 작은 경우는 안따졌다
# 주의

## 책 풀이

# 1.
# while N >= K:
#     while N % K != 0:
#         N -= 1
#         result += 1
#     N // K 
#     result += 1

# while N > 1:
#     N -= 1
#     result += 1
    
# print(result)

# 2.
# while True:
#     # (N == K로 나눠 떨어지는 수)가 될 때까지 1씩 빼기
#     target = (N // K) * K
#     result += (N - target)
#     N = target
#     # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#     if N < K:
#         break
#     # K로 나누기
#     result += 1
#     N // = K

# # 마지막으로 남은 수에 대해 1씩 빼기
# result += (N - 1)
# print(result)