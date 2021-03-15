from queue import Queue

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root_node, value):
    new_node = BinarySearchTree(value)
    if not root_node:
        root_node = new_node
    else:
        if value <= root_node.data:
            if root_node.left_child:
                insert(root_node.left_child, value)
            else:
                root_node.left_child = new_node
        else:
            if root_node.right_child:
                insert(root_node.right_child, value)
            else:
                root_node.right_child = new_node
    return value

def pre_order_traversal(root_node):
    if not root_node:
        return

    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

def in_order_traversal(root_node):
    if not root_node:
        return

    pre_order_traversal(root_node.left_child)
    print(root_node.data)
    pre_order_traversal(root_node.right_child)

def post_order_traversal(root_node):
    if not root_node:
        return

    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)
    print(root_node.data)

def level_order_traversal(root_node):
    if not root_node:
        return
    queue = Queue()
    queue.enque(root_node)
    while not queue.is_empty():
        root = queue.deque()
        print(root.data)
        if root.left_child:
            queue.enque(root.left_child)

        if root.right_child:
            queue.enque(root.right_child)

def search(root_node, value):
    if not root_node:
        return
    if root_node.data == value:
        return value
    elif value < root_node.data:
        if root_node.left_child.data == value:
            return value
        else:
            search(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            return value
        else:
            search(root_node.right_child, value)

def smallest_node(root_node):
    while root_node.left_child:
        root_node = root_node.left_child
    return root_node

def delete_node(root_node, value):
    if not root_node:
        return
    if value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = smallest_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node



bst = BinarySearchTree(70)
print(insert(bst, 50))
print(insert(bst, 90))
print(insert(bst, 30))
print(insert(bst, 60))
print(insert(bst, 80))
print(insert(bst, 100))
print(insert(bst, 20))
print(insert(bst, 40))
print("================")

level_order_traversal(bst)
print("-------------------")
print(delete_node(bst,30).data)
print("================")

level_order_traversal(bst)
# print(bst.data)
# print(bst.left_child.data)
# print(bst.left_child.left_child.data)
