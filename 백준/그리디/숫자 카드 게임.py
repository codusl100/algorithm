N, M = map(int, input().split())
# 3 X 3
new = []
arr = list(0 for i in range(M))

for i in range(N):
    arr = list()        
    arr = list(map(int, input().split()))
    arr.sort()
    n = arr[0]
    new.append(n)
new.sort(reverse=True)
print(new[0])

### 정렬해서 첫 값을 얻는 거 대신 max, min 함수 쓰면 됐겠군


## 책 풀이
# 1. min, max 함수 사용
# for i in range(n):
#     data = list(map(int, input().list()))
#     min_value = min(data)
#     result = max(result, min_value)
# print(result)

# 2. 2중 반복문
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(result, min_value)
# print(result)