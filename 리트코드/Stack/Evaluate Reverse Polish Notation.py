class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        result = 0
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(b / a))
        return int(stack[-1])