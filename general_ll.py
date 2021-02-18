from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        return len([x.value for x in self])

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self

    def generate(self, n, min_val, max_val):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_val, max_val))
        return self

# customll = LinkedList()
# customll.generate(10, 0, 90)
# print(len(customll))
def remove_dups(ll):
    if not ll.head:
        return
    node = ll.head

    visited = set([node.value])

    while node.next:
        if node.next.value in visited:
            node.next = node.next.next
        else:
            visited.add(node.next.value)
            node = node.next

    return ll

customll = LinkedList()
# customll.generate(10, 1, 99)
# print(customll)
# print(remove_dups(customll))

def nth_to_last(ll, n):
    p1 = ll.head
    p2 = ll.head

    for _ in range(n):
        if not p2:
            return
        p2 = p2.next
    while p2:
        p2 = p2.next
        p1 = p1.next
    return p1

# print(nth_to_last(customll, 101))

def partition(ll, x):
    node = ll.head
    ll.tail = node

    while node:
        next_node = node.next
        node.next = None
        if node.value < x:
            node.next = ll.head
            ll.head = node
        else:
            ll.tail.next = node
            ll.tail = node
        node = next_node
    if ll.tail.next:
        ll.tail.next = None

# partition(customll, 50)
# print(customll)

def sumll(ll1, ll2):
    node1 = ll1.head
    node2 = ll2.head
    ll = LinkedList()
    rem = 0
    while node1:
        sum = int(node1.value)+int(node2.value)+rem
        if sum > 10:
            rem = sum//10
        ll.add(sum%10)
        node1 = node1.next
        node2 = node2.next
    return ll


ll1 = LinkedList()
ll2 = LinkedList()
# ll1.add(7)
# ll1.add(1)
# ll1.add(6)

# ll2.add(5)
# ll2.add(9)
# ll2.add(2)
# print(ll1)
# print(ll2)

# print(sumll(ll1,ll2))

def intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    len1 = len(ll1)
    len2 = len(ll2)
    shorter = ll1 if len1 < len2 else ll2
    longer = ll1 if len1 > len2 else ll2
    diff = abs(len1-len2)
    print("The diff is {}".format(diff))
    longer_node = longer.head
    shorter_node = shorter.head
    
    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
        
    return shorter_node

def add_same_node(ll1,ll2, value):
    new_node = Node(value)
    ll1.tail.next = new_node
    ll1.tail = new_node

    ll2.tail.next = new_node
    ll2.tail = new_node




ll1.generate(3,1,5)
ll2.generate(3,6,9)
add_same_node(ll1,ll2,11)
add_same_node(ll1,ll2,14)
print(ll1)
print(ll2)
print(intersection(ll1,ll2))