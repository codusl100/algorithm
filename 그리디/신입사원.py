# 230122
# 백준 1946번

from sys import stdin

test_case = int(stdin.readline())

result = []

for i in range(test_case) :
    result = []
    cnt = 0
    num = int(input())
    for _ in range(num) :
        result.append(list(map(int, stdin.readline().split())))
    man_sorted = sorted(result, key = lambda x : x[0])
    
    
    man = result[0][1]
    for m in range(1, num) :
        if man_sorted[m][1] < man :
            man = man_sorted[m][1]
            cnt += 1  
    print(cnt)
    
# 이중 for문으로 시간 초과가 일어남 => 시간 초과를 해결하기 위해 for문을 하나로 줄여야함
# 첫번째 항목으로 정렬되어 있는 경우 : 이때 뒤에 있는 항이 앞에 있는 항의 [1] 값보다 값이 작으면 고용될 수 있다
# 그때 고용이 가능한 기준의 사람을 해당 사람으로 설정하고 계속해서 비교해 나간다
## 이중 for문을 없앨 때 쓰면 좋은 아이디어!! 
##  + 리스트 내의 값들을 모두 비교할 때