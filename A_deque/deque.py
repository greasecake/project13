# 52129400

class DequeIndexException(Exception):
    pass

class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            raise DequeIndexException
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise DequeIndexException
        self.head -= 1
        self.items[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise DequeIndexException
        deleted_item = self.items[self.tail]
        self.items[self.tail] = None
        self.tail -= 1
        self.size -= 1
        return deleted_item

    def pop_front(self):
        if self.size == 0:
            raise DequeIndexException
        deleted_item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return deleted_item


def handler(deque, statement):
    method_name, *args = statement
    try:
        method = getattr(deque, method_name)
        return method(*args)
    except (DequeIndexException, AttributeError):
        return 'error'


if __name__ == '__main__':
    num_statements = int(input())
    deque = Deque(int(input()))

    for _ in range(num_statements):
        statement = input().split()
    
        result = handler(deque, statement)

        if result is not None:
            print(result)
