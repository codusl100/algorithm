n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
info = []
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1
l = int(input())
for _ in range(l):
    # 왼쪽 L
    # 오른쪽 D
    time, dir = input().split() # 정수, 문자
    info.append((int(time), dir))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulation():
    x, y = 1, 1
    board[x][y] = 2
    direction = 0 # 처음에 동쪽
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulation()) 