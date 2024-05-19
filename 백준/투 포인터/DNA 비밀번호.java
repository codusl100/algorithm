from collections import Counter

s, p = map(int, input().split())
left_idx = 0
right_idx = p
arr = list(input())
a, c, g, t = map(int, input().split())
result = 0
while right_idx != s + 1:
    new_str = arr[left_idx:right_idx]
    counter = Counter(new_str)
    tmp = True
    if 'A' not in counter:
        counter['A'] = 0
    if 'C' not in counter:
        counter['C'] = 0
    if 'G' not in counter:
        counter['G'] = 0
    if 'T' not in counter:
        counter['T'] = 0
    for key in counter:
        if (key == 'A' and counter[key] < a) or (key == 'C' and counter[key] < c) or (key == 'G' and counter[key] < g) or (key == 'T' and counter[key] < t):
            tmp = False
    if tmp == True:
        result += 1
        
    left_idx += 1
    right_idx += 1
print(result)