class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        if not node:
            print("The Doubly Linked List is empty")
        else:
            while node:
                yield node
                node = node.next
                if node == self.tail:
                    break
    def insert(self, value, location=0):
        node = self.head
        new_node = Node(value)
        if not node:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            if location == 0:
                node.prev = new_node
                self.head = new_node
                new_node.next = node
                new_node.prev = self.tail
                self.tail.next = new_node
            else:
                i = 0
                while i < location-1:
                    node = node.next
                    i += 1
                
                next_node = node.next
                if node == self.tail and next_node == self.head:
                    print("The location is out of range")
                else:
                    if next_node == self.head:
                        node.next = new_node
                        next_node.prev = new_node
                        new_node.next = self.head
                        new_node.prev = node
                        self.tail = new_node
                    else:
                        new_node.next = next_node
                        new_node.prev = node
                        next_node.prev = new_node
                        node.next = new_node



circulardll = CircularDoublyLL()
print('====insert====')
circulardll.insert("Githae")
print('====insert====')
circulardll.insert("Maina",0)
print('====insert====')
circulardll.insert("Kamau",1)
print('====iter====')
print([i.value for i in circulardll])

