def solution(s):
    s_list = list(s)
    right = []
    left = []
    if s_list[0] == ')':
        return False
    else:
        for str in s_list:
            if str == '(':
                left.append(str)
                if right:
                    left.pop()
                    right.pop()
            elif str == ')':
                right.append(str)
                if left:
                    left.pop()
                    right.pop()
                else:
                    return False
        if left or right:
            return False
        else:
            return True

print(solution("()()"))