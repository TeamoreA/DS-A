class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if not self.head:
            return True
        else:
            False

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        return value

    def enque(self, value):
        if self.is_empty():
            return self.create(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            return value

    def deque(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            head = self.head
            self.head = head.next
            return head.value

    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            return self.head.value

    def delete(self):
        self.head = None
        self.tail = None
        return "Queue deleted successfully"

    def __str__(self):
        if self.is_empty():
            return "The queue is empty"
        else:
            node = self.head
            res = []

            while node:
                res.append(str(node.value))
                node = node.next

            return '\n'.join(res)
        