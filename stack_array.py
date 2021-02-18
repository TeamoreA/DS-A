class Stack:
    def __init__(self):
        self.s_list = []

    def __str__(self):
        vals = self.s_list.reverse()
        vals = [str(x) for x in self.s_list]
        return '\n'.join(vals)

    def push(self, value):
        self.s_list.append(value)
        return value

    def is_empty(self):
        if len(self.s_list) < 1:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return "No items found"
        return self.s_list.pop()

    def peek(self):
        if self.is_empty():
            return "No items found"
        return self.s_list[-1]

    def delete(self):
        self.s_list = None


s = Stack()
print("===push===")
print(s.push(1))
print("===push===")
print(s.push(2))
print("===push===")
print(s.push(3))
print("===pop===")
print(s.pop())
print("===peek===")
print(s.peek())
print("===pop===")
print(s.pop())
print("===pop===")
print(s.pop())
print("===pop===")
print(s.pop())
print("===print===")
print(s)