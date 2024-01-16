from math import sqrt
from collections import deque
import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    start, target = map(int, input().split())
    prime_number = [0 for _ in range(10000)]
    
    for i in range(2, 100):
        for j in range(2*i,10000,i):
            prime_number[j]=1

    def is_prime(i):
        return prime_number[i]==0
            
    def bfs(): # 1033, 8179
        queue = deque([int(start)]) 
        prime_number[int(start)] = 1
        while queue:
            a = queue.popleft()
            curr = str(a)
            if a == target:
                print(prime_number[int(curr)]-1)
                return
            for i in range(4):
                for j in range(10):
                    x = int(curr[:i] + str(j) + curr[i+1:])
                    if prime_number[x] == 0 and is_prime(x) and x >= 1000:
                        prime_number[x] += prime_number[a] + 1  
                        queue.append(x)
    
    bfs()
