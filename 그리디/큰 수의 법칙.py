N, M, K = map(int, input().split())

# 배열의 크기 N 5
# 숫자가 더해지는 횟수 M 8 9
# 연속 횟수 K 3 5
arr = list(map(int, input().split()))
arr.sort(reverse=True)

count = 0

first = arr[0]
second = arr[1]

m = 0
while m < M: 
    for i in range(K):
        count += first
        m += 1
    count += second
    m += 1
print(count)
        
        
        
## 책 풀이 
# while True :
#     for i in range(K):
#         if M == 0:
#             break
#         count += first
#         M -= 1
#     if M == 0 :
#         break
#     count += second
#     M -= 1
    
# print(count)           