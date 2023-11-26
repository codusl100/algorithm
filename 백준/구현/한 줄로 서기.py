N = int(input())
diff = list(map(int, input().split()))
people = [] * N

for i in range(len(diff)):
    people.insert(diff[i], i+1)
    print('누구냐', people)
print(people)

# 1 (자기보다 큰 사람 2명)
# 2 (큰 사람 1명) -> 3  
# 3 (큰 사람 1명) -> 4
# 4 (큰 사람 없음)

# 4 2 1 3 