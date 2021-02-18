class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value, location=0):
        current_node = self.head
        new_node = Node(value)
        if current_node is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                self.tail.next = new_node
                self.tail = new_node
            else:
                i = 0
                while i < location-1:
                    if  not current_node.next:
                        break
                    current_node = current_node.next
                    i += 1
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
    def traverse(self):
        node = self.head
        if not node:
            print("The list is empty")
        else:
            while node:
                print(node.value)
                node = node.next

    def search(self, value):
        node = self.head
        if not node:
            return "The list is empty"
        i = 0
        while node:
            if node.value == value:
                return i
            node = node.next
            i+=1
    def delete(self, location):
        current_node = self.head
        if not current_node:
            return "The list is empty"
        if location == 0:
            if current_node == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = None
                self.head = current_node.next
        else:
            i = 0
            while i < location-1:
                current_node = current_node.next
                i += 1
            next_node = current_node.next
            current_node.next = next_node.next


        

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


my_list = SLinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(6,7)
print("=====itter...=====")
print([node.value for node in my_list])
print("=====traverse...=====")
my_list.traverse()
print("=====search...=====")
print(my_list.search(5))
print("=====deleting...=====")
my_list.delete(0)
print([node.value for node in my_list])
