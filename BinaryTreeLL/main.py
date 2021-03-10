from queue import Queue
from stack import Stack

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right_node = None
        self.left_node = None

def preorder_traversal(node):
    if not node:
        return
    print(node.data)
    preorder_traversal(node.left_node)
    preorder_traversal(node.right_node)

def inorder_traversal(node):
    if not node:
        return

    inorder_traversal(node.left_node)
    print(node.data)
    inorder_traversal(node.right_node)

def postorder_traversal(node):
    if not node:
        return

    inorder_traversal(node.left_node)
    inorder_traversal(node.right_node)
    print(node.data)

def levelorder_traversal(node):
    if not node:
        return
    q = Queue()
    q.enqueue(node)

    while not q.is_empty():
        root = q.dequeue()
        if root.data:
            print(root.data)
        if root.left_node:
            q.enqueue(root.left_node)
        if root.right_node:
            q.enqueue(root.right_node)

tree_level = 0
nodes = []
def nodes_list(node):
    global tree_level
    if not node:
        return
    
    level_nodes = [node]
    if tree_level == 0:
        nodes.append(node.data)
    for node in level_nodes:
        tree_level += 1
        level_nodes = []
        if node.left_node:
            level_nodes.append(node.left_node)
            nodes.append(node.left_node.data)
        if node.right_node:
            level_nodes.append(node.right_node)
            nodes.append(node.right_node.data)

    for node in level_nodes:
        nodes_list(node)
    return nodes


def search_bt(node, val):
    n_list = nodes_list(node)
    if val in n_list:
        return val

    return "Not found"

def get_parent(node, val):
    if not node:
        return
    q = Queue()
    q.enqueue(node)

    while not q.is_empty():
        root = q.dequeue()
        if root.left_node:
            if root.left_node.data == val:
                return root, 'left'
            q.enqueue(root.left_node)
        if root.right_node:
            if root.right_node == val:
                return root, 'right'
            q.enqueue(root.right_node)


def deepest_node(node):
    if not node:
        return
    s = Stack()
    s.push(node)

    while not s.is_empty():
        root = s.pop()
        # print(root.data)
        if root.left_node:
            s.push(root.left_node)
        if root.right_node:
            s.push(root.right_node)

    return root

def last_node(node):
    if not node:
        return
    q = Queue()
    q.enqueue(node)

    while not q.is_empty():
        root = q.dequeue()
        # print(root.data)
        if root.left_node:
            q.enqueue(root.left_node)
        if root.right_node:
            q.enqueue(root.right_node)

    return root

def insert_bt(node, new_value):
    new_node = TreeNode(new_value)
    d_node = deepest_node(node)
    d_node.left_node = new_node
    return new_value

def delete_bt(root_node, to_delete):
    l_node = last_node(root_node)
    to_delete.data = l_node.data
    l_node.data = None
    return to_delete.data
    


new_bt = TreeNode("Drinks")

cold = TreeNode("Cold")
hot = TreeNode("Hot")

cola = TreeNode("cola")
fanta = TreeNode("fanta")
coffee = TreeNode("coffee")
tea = TreeNode("tea")

new_bt.left_node = cold
new_bt.right_node = hot

cold.left_node = cola
cold.right_node = fanta

hot.left_node = coffee
hot.right_node = tea



# preorder_traversal(new_bt)

# inorder_traversal(new_bt)

# postorder_traversal(new_bt)
# print("+++++++++++++++")
print(insert_bt(new_bt, "pepsi"))
# print(insert_bt(new_bt, "coke"))
print("===============")
# p,s = get_parent(new_bt, hot)
# print(s.data)
print(delete_bt(new_bt, hot))
print("===============")
levelorder_traversal(new_bt)

# print(deepest_node(new_bt))
# print(deepest_node(new_bt).data)
# print(search_bt(new_bt, 'Hot'))