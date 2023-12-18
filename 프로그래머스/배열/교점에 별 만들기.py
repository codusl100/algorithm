def solution(line):
    x_points = []
    y_points = []
    points = []
    # line for문으로 돌리면서 교점 찾기
    for i in range(len(line)-1):
        a = line[i][0]*line[i+1][1] - line[i][1]*line[i+1][0]
        if a != 0: # 교점이 있으면
            x = line[i][1]*line[i+1][2] - line[i][2]*line[i+1][1] // a
            y = line[i][2]*line[i+1][0] - line[i][0]*line[i+1][2] // a
            x_points.append(x)
            y_points.append(y)
            points.append([x, y])
    # 마지막 항이랑 첫 항 비교
    if line[-1][0]*line[0][1] - line[-1][1]*line[0][0] != 0:
        x = line[-1][1]*line[0][2] - line[-1][2]*line[0][1] // line[-1][0]*line[0][1] - line[-1][1]*line[0][0]
        y = line[-1][2]*line[0][0] - line[-1][0]*line[0][2] // line[-1][0]*line[0][1] - line[-1][1]*line[0][0]
        x_points.append(x)
        y_points.append(y)
        points.append([x, y])

    # 찾고 난 뒤 절댓값 젤 큰거 찾고 배열 크기 선언
    x_min, x_max = min(x_points), max(x_points)  # 교점의 x좌표들 중 최소값과 최대값
    y_min, y_max = min(y_points), max(y_points)  # 교점의 y좌표들 중 최소값과 최대값

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in points:
        answer[y_max - y][x - x_min] = '*'  # 교점에 별 만들기
    answer.reverse()
    return list(map(''.join, answer))

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))