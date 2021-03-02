class StackOfPlates:
    def __init__(self, limit=3):
        self.stacks = []
        self.limit = limit

    def __str__(self):
        return str(self.stacks)

    def push(self, value):
        curr_stack = len(self.stacks)
        if curr_stack > 0 and len(self.stacks[-1]) < self.limit:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

        return value

    def pop(self):
        if len(self.stacks[-1]) == 1:
            val = self.stacks[-1][0]
            self.stacks.pop()
            return val
        else:
            return self.stacks[-1].pop()

    def pop_at(self, index):
        if len(self.stacks) <= index:
            return "The index is out range"
        if len(self.stacks[index]) == 1:
            val = self.stacks[index][0]
            self.stacks.pop(index)
            return val
        else:
            return self.stacks[index].pop()




sop = StackOfPlates()
sop.push(0)
sop.push(1)
sop.push(2)
sop.push(3)
sop.push(4)
sop.push(5)
sop.push(6)
print(sop.pop())
print(sop.pop_at(0))
print(sop.pop_at(0))
print(sop.pop_at(1))
print(sop.pop_at(1))
print(sop)