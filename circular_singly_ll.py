class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def add(self, value, location=0):
        node = self.head
        new_node = Node(value)
        if not node:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            i = 0
            if location == 0:
                new_node.next = node
                self.head = new_node
                self.tail.next = new_node
            else:
                while i < location-1:
                    node = node.next
                    i += 1
                if node == self.tail:
                    node.next = new_node
                    new_node.next = self.head
                    self.tail = new_node
                else:
                    new_node.next = node.next
                    node.next = new_node

    def traverse(self):
        # print all items in the CircularSLL
        node = self.head
        if not node:
            print('The list is empty')
        else:
            while node:
                # loop though the nodes
                print(node.value)
                if node == self.tail:
                    break
                node = node.next

    def search(self, value):
        node = self.head
        if not node:
            print('The list is empty')
        i = 0
        while node:
            if node.value == value:
                return ([value, i])
            i += 1
            node = node.next
            if node == self.head:
                return ('Node not found')


    def delete(self, value):
        node = self.head
        if not node:
            return ('The list is empty')
        if value == node.value:
            if node == node.next:
                self.head = None
                self.tail = None
                node.next = None
            else:
                self.head = node.next
                self.tail.next = node.next
            return value
        else:
            while node:
                
                if node.next.value == value:
                    if node.next == self.tail:
                        self.tail = node
                        node.next = self.head
                        # return value
                    else:
                        to_delete = node.next
                        node.next = to_delete.next
                    return value
                node = node.next
                if node == self.head:
                    return 'Node not found'

    def clear(self):
        node = self.head
        if not node:
            return "The list is empty"
        self.head = None
        self.tail.next = None
        self.tail = None
        return "The list has been cleared"
        



circularsll = CircularSLL()
print("\n\t----traverse----")
circularsll.traverse()
print('\n\t-----add 1----')
circularsll.add(1)
circularsll.traverse()
# print('\n\t-----delete-----')
# print(circularsll.delete(1))
print('\n\t-----add 2----')
circularsll.add(2)
circularsll.traverse()
print('\n\t-----add 3----')
circularsll.add(3,2)
circularsll.traverse()
print('\n\t-----clear-----')
print(circularsll.clear())
print("\n\t----traverse----")
circularsll.traverse()
print('\n\t-----search 3-----')
print(circularsll.search(3))

print('\n\t-----delete 2-----')
print(circularsll.delete(2))
print("\n\t----traverse----")
circularsll.traverse()
print('\n\t-----delete 1-----')
print(circularsll.delete(1))
print("\n\t----traverse----")
circularsll.traverse()
print('\n\t-----delete 3-----')
print(circularsll.delete(3))
print("\n\t----traverse----")
circularsll.traverse()
print('\n\t-----delete 3-----')
print(circularsll.delete(3))
print('\n\t-----iterate-----')
print([i.value for i in circularsll])
                