class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1

def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance(parent):
    hDiff = calc_height_diff(parent)
    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

def insert_avl(parent, node):
    if parent is None:
        return node
    if node.key < parent.key:
        parent.left = insert_avl(parent.left, node)
    elif node.key > parent.key:
        parent.right = insert_avl(parent.right, node)
    else:
        print("중복된 키 에러")
        return parent

    return reBalance(parent)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_avl(parent, key):
    if parent is None:
        return parent

    if key < parent.key:
        parent.left = delete_avl(parent.left, key)
    elif key > parent.key:
        parent.right = delete_avl(parent.right, key)
    else:
        # 노드가 발견됨
        if parent.left is None:
            return parent.right
        elif parent.right is None:
            return parent.left
        else:
            min_larger_node = find_min(parent.right)
            parent.key = min_larger_node.key
            parent.right = delete_avl(parent.right, min_larger_node.key)

    return reBalance(parent)

def count_node(n):
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    if n.left is None and n.right is None:
        return 1
    return count_leaf(n.left) + count_leaf(n.right)

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        return item

    def isEmpty(self):
        return self.front == self.rear

def levelorder(root):
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]

    root = None
    for i in node:
        n = BSTNode(i)
        root = insert_avl(root, n)
        print("AVL(%d): " % i, end='')
        levelorder(root)
        print()

    print("노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))

    # 삭제 테스트
    keys_to_delete = [3, 6, 8]
    for key in keys_to_delete:
        print("삭제할 키:", key)
        root = delete_avl(root, key)
        levelorder(root)
        print()

    print("삭제 후 노드의 개수 =", count_node(root))
    print("삭제 후 단말의 개수 =", count_leaf(root))
    print("삭제 후 트리의 높이 =", calc_height(root))
