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
            print("The CDLL is empty")
        else:
            while node:
                yield node
                node = node.next
                if node == self.tail.next:
                    break

    def create(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        print("CDLL created successfuly")

    def search(self, value):
        node = self.head
        if not Node:
            return "The CDLL is empty"
        i = 0
        while node:
            if node.value == value:
                return [value, i]
            node = node.next
            i += 1
            if node == self.tail.next:
                break
        return "The value is not found"

    def traverse(self):
        node = self.head
        if not node:
            print("The CDLL is empty")
        else:
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    def reverse_traverse(self):
        node = self.tail
        if not node:
            print('The CDLL is empty')
        else:
            while node:
                print(node.value)
                node = node.prev
                if node == self.head.prev:
                    break

    def delete(self, value):
        node = self.head
        if not node:
            return "The CDLL is empty"
        temp_node = node.next
        if value == self.head.value:
            self.tail.next = temp_node
            temp_node.prev = self.tail
            self.head = temp_node
            return value
        elif value == self.tail.value:
            self.tail.prev.next = self.head
            self.head.next = self.tail.prev
            self.tail = self.tail.prev
            return value
        else:
            while temp_node:
                if temp_node == self.tail:
                    break
                if temp_node.value == value:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev
                    return value
                temp_node = temp_node.next
        return "{} not found in the CDLL".format(value)

    def delete_multiple(self, values):
        for val in values:
            self.delete(val)
    def clear(self):
        node = self.head
        if not node:
            print("The CDLL is empty")
        else:
            while node:
                node.next = None
                node = node.next
            self.head = None
            self.tail = None
            print("CDLL cleared successfuly")


    def insert(self, value, location=0):
        node = self.head
        new_node = Node(value)
        if not node:
            self.create(value)
        else:
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
                print("Head element added successfuly")
            else:
                i = 0
                while i < location-1:
                    node = node.next
                    i += 1
                    if node == self.tail.next:
                        break
                
                if node == self.tail:
                    new_node.next = self.head
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.head.prev = new_node
                    self.tail = new_node
                    print("Tail element added successfuly")
                else:
                    new_node.next = node.next
                    new_node.prev = node
                    node.next.prev = new_node
                    node.next = new_node
                    print("New element added at location {}".format(location))



circulardll = CircularDoublyLL()
print('====create====')
circulardll.create("Githae")
print('====insert====')
circulardll.insert("Maina",1)
print('====insert====')
circulardll.insert("Kamau",2)
print("====search===")
print(circulardll.search("Githae"))
print('====traverse====')
circulardll.traverse()
print('====reverse_traverse====')
circulardll.reverse_traverse()
# print('====delete====')
# print(circulardll.delete("Maina"))
# print('====delete_multiple====')
# print(circulardll.delete_multiple(['Kamau',"Maina"]))
# print("====clear====")
# circulardll.clear()
# circulardll.clear()
print('====iter====')
print([i.value for i in circulardll])

