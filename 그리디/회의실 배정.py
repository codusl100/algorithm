# 230117
# 백준 1931번

# N = int(input())
# arr = list()
# for i in range(N) :
#     arr.append(list(map(int, input().split())))
# arr.sort()

# time = list()

# min = arr[0]
# num = 0

# for i in range(1, len(arr)) :
#     if min[0] <= arr[i][0] and min[1] <= arr[i][1] :
#         min = arr[i]
#         time.append(min) 
#     if min[0] <= arr[i][0] and arr[i][1] <= min[1] :
#         min = arr[i]
#         num = i
#         time.append(min)
        
# for i in range(num + 1, len(arr)) :
#     if min[1] <= arr[i][0] :
#         min = arr[i]
#         time.append(min)
#     elif min == arr[i] :
#         time.append(arr[i])

# print(time)
# print(len(time))

# 위에처럼 풀었을 때 예제의 답은 맞으나 회의시간의 시작, 끝나는 시간이 같을 때 계속 틀렸음
# 문제를 풀면서 고려해야하는 점은 빨리 끝나는 순으로 정렬해야 한다
# 그리고 끝나는 시간이 같다면 빨리 시작하는 순으로 정렬되어야 한다
# 문제풀이 방법
# 1. 전체를 시작시간의 오름차순으로 정렬한 후 정렬된 리스트를 다시 끝나는 시간대로 정렬하기
# => 이미 시작시간 오름차순으로 정렬되어 있기에 끝나는 시간이 같을 때 시작 시간의 오름차순으로 정렬됨
# 2. 한번에 정렬 (Key에 튜플로 여러 인자를 주면 해당 인자의 순서대로 정렬을 해준다)

## 2차원 요소를 기준으로 정렬할 때 sorted(list, key = lambda a:a[n]) 사용

n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)