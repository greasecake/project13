# 52129834

from operator import add, sub, mul, floordiv


OPERATOR_DICT = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


class StackIndexError(Exception):
    pass


class UnsupportedCharacter(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise StackIndexError

    def push(self, item):
        self.items.append(item)


def calculate(characters):
    stack = Stack()
    for character in characters:
        try:
            operation = OPERATOR_DICT[character]
        except KeyError:
            try:
                operand = int(character)
            except ValueError:
                raise UnsupportedCharacter
            else:
                stack.push(operand)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            result = operation(operand_1, operand_2)
            stack.push(result)
    return stack.pop()


if __name__ == '__main__':
    print(calculate(input().split()))
