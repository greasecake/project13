def math(operand_1, operand_2, operator):
    if operator == '+':
        return operand_1 + operand_2
    if operator == '-':
        return operand_1 - operand_2
    if operator == '*':
        return operand_1 * operand_2
    if operator == '/':
        return operand_1 // operand_2

stack = []
for i in input().split():
    try:
        operand = int(i)
        stack.append(operand)
    except ValueError:
        result = math(stack.pop(), stack.pop(), i)
        stack.append(result)
print(stack.pop())