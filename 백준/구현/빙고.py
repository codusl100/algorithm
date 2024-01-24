graph = [[0] for i in range(5)]
graph_list = []

for i in range(5):
    graph[i] = list(map(int, input().split()))
    # 가로 추가
    graph_list.append(graph[i])

# 세로 추가
for i in range(5):
    column = []
    for j in range(5):
        column.append(graph[j][i])
    graph_list.append(column)

# 대각선 추가
temp = []
for i in range(5):
    temp.append(graph[i][i])
graph_list.append(temp)

temp = []
for i in range(5):
    temp.append(graph[i][4-i])
graph_list.append(temp)

call = [int(x) for _ in range(5) for x in input().split()]

cnt = 0
min_cnt = 26
bingo = 0

for i in range(len(call)):
    # graph_list 조회해서 방문 체크
    for j in range(12):
        for k in range(5):
            if graph_list[j][k] == call[i]:
                graph_list[j][k] = 0
    cnt += 1
    
    # 한 줄 빙고 발견하면 
    for j in range(12):
        if all(element == 0 for element in graph_list[j]):
            graph_list[j] = [1, 1, 1, 1, 1]
            bingo += 1
        if bingo == 3:
            min_cnt = min(cnt, min_cnt)
            break
print(min_cnt)