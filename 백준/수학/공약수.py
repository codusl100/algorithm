import sys
from math import sqrt

input = sys.stdin.readline

g, l = map(int, input().split()) # 최대공약수, 최소공배수
divide = l // g # a*b = l/g

def gcd(a, b):
	while a % b != 0:
		tmp = a % b
		a = b
		b = tmp
	return b

for a in range(int(sqrt(divide)), 0, -1):
    b = int(divide / a) # b = (l/g)/a
	
    if divide % a == 0 and gcd(a, b) == 1: # 약수고 서로소면
        print(a*g, b*g)
        break