nan = [int(input()) for i in range(9)]
total = sum(nan)
twoBreak = True
nan.sort() 

for a in range(0, len(nan)-1) :
    for b in range(a+1, len(nan)) :
        if total - nan[a] - nan[b]  == 100 :
            nan.remove(nan[b])
            nan.remove(nan[a])
            twoBreak = False
            break
    if twoBreak == False :
        break
    
for i in range(len(nan)):
    print(nan[i])