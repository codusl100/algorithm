def solution(number, k): # number = 1, 2, 3, 1, 2, 3, 4
    stack = []
    for i in number : 
        while k > 0 and stack and stack[-1] < i : 
            k -= 1
            stack.pop()
        stack.append(i)    
    return ''.join(stack[:len(stack) - k])