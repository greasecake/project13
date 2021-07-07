class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            return 'error'
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            return 'error'
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            return 'error'
        self.tail = (self.tail - 1) % self.max_size
        deleted_item = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        return deleted_item

    def pop_front(self):
        if self.size == 0:
            return 'error'
        deleted_item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return deleted_item

    # def blank(self):
    #     pass

    # def print_items(self):
    #     return self.items
    
    # def print_head(self):
    #     return self.items[self.head : self.max_size+1-self.head] + self.items[0 : self.head]


if __name__ == '__main__':
    statements_num = int(input())
    max_size = int(input())
    deque = Deque(max_size)

    for i in range(statements_num):
        method_name, *args = input().split()
        args = list(map(int, args))

        method = getattr(deque, method_name)
        result = method(*args)

        if result is not None:
            print(result)
