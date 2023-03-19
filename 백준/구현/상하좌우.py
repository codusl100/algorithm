# 예제 4-1
# N = int(input())

# dir = list(map(str, input().split()))
# Xpos = 0
# Ypos = 0

# for i in range(len(dir)) :
#     if dir[i] == 'L':
#         if Xpos <= 0 :
#             Xpos = 0
#         else :
#             Xpos -= 1
#     elif dir[i] == 'R':
#         if Xpos >= N :
#             Xpos = N
#         else :
#             Xpos += 1
#     elif dir[i] == 'U':
#         if Ypos >= N :
#             Ypos = N
#         else :
#             Ypos += 1
#     elif dir[i] == 'D':
#         if Ypos <= 0 :
#             Ypos = 0
#         else :
#             Ypos -= 1

# 책에서는 비교 연산을 줄였다! 이 방법을 새겨보자
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)