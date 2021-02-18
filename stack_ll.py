class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        # check if empty O(1)
        if not self.head:
            return True
        return False

    def __str__(self):
        # string representation O(n)
        if self.is_empty():
            return "No values found"
        node = self.head
        stack_l = []
        while node:
            stack_l.append(str(node.value))
            node = node.next
        return '\n'.join(stack_l)

    def len(self):
        # length O(n)
        if self.is_empty():
            return "No values found"
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def push(self, value):
        # push O(1)
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = None
        else:
            new_node.next = self.head
            self.head = new_node
        return value

    def pop(self):
        # pop O(1)
        if self.is_empty():
            return "No values found"
        val = self.head.value
        self.head = self.head.next
        return val

    def peek(self):
        # peek O(1)
        if self.is_empty():
            return "No values found"
        return self.head.value

    def delete(self):
        # delete O(1)
        if self.is_empty():
            return "No values found"
        self.head = None
        self.tail = None
        return "The stack has been cleared"



stack = Stack()
print("+++push+++")
print(stack.push(1))
print("+++push+++")
print(stack.push(2))
print("+++push+++")
print(stack.push(3))
print("+++push+++")
print(stack.push(4))
print("+++peek+++")
print(stack.peek())
print("+++print+++")
print(stack)
print("+++pop+++")
print(stack.pop())
print("+++print+++")
print(stack)
print("+++len+++")
print(stack.len())
print("+++delete+++")
print(stack.delete())
print("+++print+++")
print(stack)
