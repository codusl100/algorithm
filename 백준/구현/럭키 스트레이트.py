arr = [int(i) for i in input()]
N = len(arr) // 2
temp1 = 0
temp2 = 0
for i in range(N):
    temp1 += arr[i]

for i in range(N, len(arr)):
    temp2 += arr[i]

if temp1 == temp2:
    print('LUCKY')
else:
    print('READY')