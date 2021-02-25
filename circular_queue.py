class CircularQueue:
    def __init__(self, limit=10):
        self.items = limit * [None]
        self.limit = limit
        self.start = -1
        self.top = -1

    def __str__(self):
        return '\n'.join([str(i) for i in self.items if i is not None])

    def is_empty(self):
        if self.top ==  -1:
            return True
        else:
            return False


    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.limit:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return "The queue is full"
        else:
            if self.top+1 == self.limit:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return value



cq = CircularQueue(10)
print("+++is full+++")
print(cq.is_full())
print("+++is_empty+++")
print(cq.is_empty())
print("+++enqueue+++")
print(cq.enqueue(1))
print("+++enqueue+++")
print(cq.enqueue(2))
print("+++enqueue+++")
print(cq.enqueue(3))
print("+++print+++")
print(cq)
