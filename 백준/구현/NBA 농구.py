# goal_1 = 0
# goal_2 = 0

# time_1 = list()
# time_2 = list()
# H = 48
# M = 0

# new_H_1 = 0
# new_M_1 = 0
# bool1 = False

# new_H_2 = 0
# new_M_2 = 0
# bool2 = False

# goal = int(input())
# for i in range(goal) : # 3
#     team = int(input()) # 1     48:00  2
#     h, m = input().split(':') # 01:10  21:10
    
#     if team == 1 :
#         goal_1 += 1    #1
#     else :
#         goal_2 += 1    #1
    
#     if goal_1 > goal_2 :
#         if h <= new_H_1 and m <= new_M_1 :
#             new_H_1 = h
#             new_M_1 = m
#         bool1 = True # 1이 마지막으로 골 넣음
#         bool2 = False
#     elif goal_1 < goal_2 :
#         if h <= new_H_2 and m <= new_M_2 :
#             new_H_2 = h
#             new_M_2 = m
#         bool1 = False # 2이 마지막으로 골 넣음   
#         bool2 = True
#     else : # 동점일때
#         if team == 1 : # 1팀이 골 넣었다면
#             if bool2 == True : # 마지막에 2팀이 골 넣었으면
#                 new_H_1 = h - new_H_1
#                 if m - new_M_1 < 0 :
#                     new_M_1 = 60 + m - new_M_1
#                 else :
#                     new_M_1 = m - new_M_1                
#         else : # 2팀이 골 넣었다면
#             if bool1 == True : # 마지막에 1팀이 골 넣었으면
#                 new_H_2 = h - new_H_2
#                 if m - new_M_2 < 0 :
#                     new_M_2 = 60 + m - new_M_2
#                 else :
#                     new_M_2 = m - new_M_2

N = int(input())

time_1 = 0
time_2 = 0
end = 48 * 60
win = 0
# 시간, 분을 그냥 분으로 통일
for i in range(N) :
    team, goal = input().split()
    min, sec = map(int, goal.split(':'))
    time = min * 60 + sec
    # 1번팀이 점수 획득시 양수, 2번팀이 점수 획득시 음수
    if team == '1' :
        if win == 0 :
            time_1 += (end - time)
        win += 1
        if win == 0 : # 득점 우위 바뀜
            time_2 -= (end - time)
    else :
        if win == 0 :
            time_2 += (end - time)
        win -= 1
        if win == 0 :
            time_1 -= (end - time)
            
print('{:0>2}:{:0>2}'.format((time_1)//60, (time_1)%60))
print('{:0>2}:{:0>2}'.format((time_2)//60, (time_2)%60))