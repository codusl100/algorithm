# 예제 4-1
N = int(input())

dir = list(map(str, input().split()))
Xpos = 0
Ypos = 0

for i in range(len(dir)) :
    if dir[i] == 'L':
        if Xpos <= 0 :
            Xpos = 0
        else :
            Xpos -= 1
    elif dir[i] == 'R':
        if Xpos >= N :
            Xpos = N
        else :
            Xpos += 1
    elif dir[i] == 'U':
        if Ypos >= N :
            Ypos = N
        else :
            Ypos += 1
    elif dir[i] == 'D':
        if Ypos <= 0 :
            Ypos = 0
        else :
            Ypos -= 1