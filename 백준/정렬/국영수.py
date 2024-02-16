n = int(input())
arr = []
for i in range(n):
    name, x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    arr.append([name, x, y, z])
arr.sort(key=lambda a: (-a[1], a[2], -a[3], a[0]))
for student in arr:
    print(student[0])