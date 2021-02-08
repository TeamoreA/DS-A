class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def create(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        return "The DLL has been created"
    
    def traverse(self):
        current_node = self.head
        if not current_node:
            print("The list is empty")
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        current_node = self.tail
        if not current_node:
            print("The list is empty")
        else:
            while current_node:
                print(current_node.value)
                current_node = current_node.prev

    def delete(self, value):
        node = self.head
        if not node:
            print("The list is empty")
        else:
            if value == self.head.value:
                next_node = self.head.next
                self.head = next_node
                next_node.prev = None
            elif value == self.tail.value:
                prev_node = self.tail.prev
                self.tail = prev_node
                prev_node.next = None
            else:
                while node:
                    if node.value == value:
                        prev_node = node.prev
                        next_node = node.next
                        prev_node.next = next_node
                        next_node.prev = prev_node
                    node = node.next

    def delete_multiple(self, values):
        for i in values:
            self.delete(i)

    def search(self, value):
        node = self.head
        if not node:
            print("The list is empty")
        else:
            i = 0
            while node:
                if value == node.value:
                    print([value, i])
                if node == self.tail and value != node.value:
                    print("Value not found in the list")
                i += 1
                node = node.next

    def insert(self, value, location=0):
        current_node = self.head
        new_node = Node(value)
        if not current_node:
            self.create(value)
        else:
            if location == 0:
                current_node.prev = new_node
                self.head = new_node
                new_node.next = current_node
            else:
                i = 0
                while i < location:
                    current_node = current_node.next
                    i += 1
                    if not current_node:
                        return "Location is out of range"
                if current_node == self.tail:
                    new_node.prev = current_node
                    current_node.next = new_node
                    self.tail = new_node
                else:
                    next_node = current_node.next
                    current_node.next = new_node
                    new_node.next = next_node
                    new_node.prev = current_node
                    next_node.prev = new_node
                    
        return value



doublyll = DoublyLinkedList()
print("====create====")
print(doublyll.create(1))
print("====insert====")
print(doublyll.insert(2))
print("====insert====")
print(doublyll.insert(3))
print("====insert====")
print(doublyll.insert(4))
print("====insert====")
print(doublyll.insert(5,3))
print("===traverse====")
doublyll.traverse()
print("===reverse_traverse====")
doublyll.reverse_traverse()
print("===search====")
doublyll.search(5)
print("===delete====")
doublyll.delete(2)
print("===delete_multiple====")
doublyll.delete_multiple([1,2,3])
print('====iter====')
print([i.value for i in doublyll])