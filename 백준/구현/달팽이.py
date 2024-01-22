import sys
input = sys.stdin.readline

n = int(input())
find = int(input())

graph = [[0] * n for i in range(n)]

start_x = n // 2
start_y = n // 2

curr_x = start_x
curr_y = start_y

status = 'UP'

graph[curr_y][curr_x] = 1

ans_x = 0
ans_y = 0


for i in range(2, n*n + 1):
    if status == 'UP' and curr_y - 1 >= 0:
        curr_y -= 1
        if graph[curr_y][curr_x + 1] == 0:            
            status = 'RIGHT'
    elif status == 'RIGHT' and curr_x + 1 < n:
        curr_x += 1
        if graph[curr_y + 1][curr_x] == 0:
            status = 'DOWN' 
    elif status == 'DOWN' and curr_y + 1 < n:
        curr_y += 1
        if graph[curr_y][curr_x - 1] == 0:
            status = 'LEFT'
    elif status == 'LEFT' and curr_x - 1 >= 0:
        curr_x -= 1
        if graph[curr_y - 1][curr_x] == 0:
            status = 'UP'
    graph[curr_y][curr_x] = i
    if i == find:
        ans_x = curr_x
        ans_y = curr_y
if find == 1:
    ans_x = start_x
    ans_y = start_y
for i in graph:
    for j in i:
        print(j, end = ' ')
    print()
print(str(ans_y+1)+" "+str(ans_x+1))