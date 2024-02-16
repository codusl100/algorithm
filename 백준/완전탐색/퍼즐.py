from collections import deque
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board_size = 3

def bfs(start):
    queue = deque([(start)])
    board[start] = 0
    while queue:
        now = queue.popleft()
        if now == '123456780':
            return board[now]
        loc = now.find('0') # 위치
        nowx, nowy = loc % board_size, loc // board_size

        for i in range(4):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            nloc = ny*3 + nx
            if nx < 0 or nx >= board_size or ny < 0 or ny >= board_size:
                continue
            nowList = list(now)
            nowList[loc], nowList[nloc] = nowList[nloc], nowList[loc]
            nxt = ''.join(nowList)
            if not board.get(nxt):
                board[nxt] = board[now] + 1
                queue.append(nxt)
    return -1

board = {}
nowInput = ''
for i in range(board_size):
    nowInput += ''.join(input().split(' '))
print(bfs(nowInput))