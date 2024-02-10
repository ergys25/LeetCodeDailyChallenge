class Solution:
    def calculate(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)
        return 0

    def eval_rpn(self, tokens):
        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                if len(stack) < 2:
                    return 0
                num2 = stack.pop()
                num1 = stack.pop()
                operator = token
                result = self.calculate(num1, num2, operator)
                stack.append(result)
            else:
                stack.append(int(token))
        if len(stack) == 1:
            return stack.pop()
        else:
            return 0  # Handle case where there are extra operands in the stack
