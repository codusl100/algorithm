import sys
input = sys.stdin.readline
N, people = map(int, input().split())
namelist = []
powerlist = []
result = []
for i in range(N):
    nickname, power = input().split()
    namelist.append(nickname)
    powerlist.append(int(power))

start = 0 
end = N-1 # 2

def binary(a):
    start = 0 
    end = N-1
    while start <= end :
        mid = (start + end) // 2
        if a > powerlist[mid]:
            start = mid + 1
        else :
            end = mid - 1
    print(namelist[end+1])
    
for i in range(people):
    a = int(input())
    binary(a)