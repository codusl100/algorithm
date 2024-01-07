from itertools import combinations

def find_point(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if a * d == b * c:
        return
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c - a*f) / (a*d - b*c)
    if x == int(x) and y == int(y): # 교점이 정수라면
        return (int(x), int(y))

def solution(line):
    x_points, y_points = set(), set()
    points = set()

    for a, b in combinations(line, 2):
        point = find_point(a, b)
        if point:
            points.add(point)
            x_points.add(point[0])
            y_points.add(point[1])

    # 찾고 난 뒤 절댓값 젤 큰거 찾고 배열 크기 선언
    x_min, x_max = min(x_points), max(x_points)
    y_min, y_max = min(y_points), max(y_points)

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in points:
        answer[y_max - y][x - x_min] = '*'  # 교점에 별 만들기
    return list(map(''.join, answer))

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))