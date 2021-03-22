class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def pre_order_traversal(root_node):
    if root_node is None:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if root_node is None:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if root_node is None:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if root_node is None:
        return
    nodes = []
    nodes.append(root_node)
    while nodes != []:
        root = nodes.pop(0)
        print(root.data)
        if root.left_child is not None:
            nodes.append(root.left_child)
        if root.right_child is not None:
            nodes.append(root.right_child)


def search(root_node, value):
    if root_node.data == value:
        return value
    elif value < root_node.data:
        if root_node.left_child.data == value:
            return value
        else:
            search(root_node.left_child, value)
    else:
        if root_node.left_child.data == value:
            return value
        else:
            search(root_node.right_child, value)


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def rotate_right(unbalanced_node):
    new_root = unbalanced_node.left_child
    unbalanced_node.left_child = unbalanced_node.left_child.right_child
    new_root.right_child = unbalanced_node
    unbalanced_node.height = 1 + max(get_height(unbalanced_node.left_child),
                                     get_height(unbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child),
                              get_height(new_root.right_child))
    return new_root


def rotate_left(unbalanced_node):
    new_root = unbalanced_node.right_child
    unbalanced_node.right_child = unbalanced_node.right_child.left_child
    new_root.left_child = unbalanced_node
    unbalanced_node.height = 1 + max(get_height(unbalanced_node.left_child),
                                     get_height(unbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child),
                              get_height(new_root.right_child))
    return new_root


def get_difference(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)


def insert(root_node, value):
    if not root_node:
        return AVLNode(value)
    elif value <= root_node.data:
        root_node.left_child = insert(root_node.left_child, value)
    else:
        root_node.right_child = insert(root_node.right_child, value)

    root_node.height = 1 + max(get_height(root_node.left_child),
                               get_height(root_node.right_child))
    diff = get_difference(root_node)
    if diff > 1 and value < root_node.left_child.data:
        # left - left condition
        return rotate_right(root_node)

    if diff > 1 and value > root_node.left_child.data:
        # left - right condition
        root_node.left_child = rotate_left(root_node.left_child)
        return rotate_right(root_node)

    if diff < -1 and value > root_node.right_child.data:
        # right - right condition
        return rotate_left(root_node)

    if diff < -1 and value < root_node.right_child.data:
        # right - left condition
        root_node.right_child = rotate_right(root_node.right_child)
        return rotate_left(root_node)
    return root_node

def get_min_node(root_node):
    if not root_node or not root_node.left_child:
        return root_node
    get_min_node(root_node.left_child)

def delete_node(root_node, value):
    if not root_node:
        return
    elif value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child is  None:
            temp = root_node.right_child
            root_node = None
            return temp
        elif root_node.right_child is  None:
            temp = root_node.left_child
            root_node = None
            return temp
        temp = get_min_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    diff = get_difference(root_node)
    if diff > 1 and get_difference(root_node.left_child) >= 0: #ll
        return rotate_right(root_node)
    if diff < -1 and get_difference(root_node.right_child) >= 0: #rr
        return rotate_left(root_node)
    if diff > 1 and get_difference(root_node.left_child) < 0: #lr
        root_node.left_child = rotate_left(root_node.left_child)
        return rotate_right(root_node)

    if diff < -1 and get_difference(root_node.right_child) < 0: #rl
        root_node.right_child = rotate_right(root_node.right_child)
        return rotate_left(root_node)

    return root_node


avl = AVLNode(5)
avl = insert(avl, 10)
avl = insert(avl, 15)
avl = insert(avl, 20)
print('______________')
print(level_order_traversal(avl))
print('______________')
print(delete_node(avl, 10).data)
print('______________')
print(level_order_traversal(avl))

