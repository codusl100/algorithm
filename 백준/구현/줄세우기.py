P = int(input())

for _ in range(P):
    line = input().split() # 0 ~ 20
    students = []
    ans = 0
    for i in range(1, 21): #3 915 - 차례대로 넣을 애들
        for j in range(i): #기존에 있는 애들
            if int(line[i]) < int(line[j]) and int(line[i]) not in students:
                students.insert(j-1, int(line[i]))
                ans += i - j 
    print(int(line[0]), ans, sep=' ')