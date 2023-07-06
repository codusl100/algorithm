N = int(input())
box = list()
count = 0

for i in range(N):
    box.append(int(input()))

box.sort(reverse=True)

for i in range(len(box)):
    if (i+1) % 3 != 0 :
        count += box[i]
print(count)