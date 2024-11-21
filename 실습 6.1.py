class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return self.search_max_bst(self.root)

    def findMin(self):
        return self.search_min_bst(self.root)

    def search(self, key):
        return self.search_bst(self.root, key)

    def searchValue(self, key):
        return self.search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.insert_bst(self.root, n)

    def delete(self, key):
        self.root = self.delete_bst(self.root, key)

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)
            print(n.key, end=' ')
            self.inorder(n.right)

    def preorder(self, n):
        if n is not None:
            print(n.key, end=' ')
            self.preorder(n.left)
            self.preorder(n.right)

    def postorder(self, n):
        if n is not None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.key, end=' ')

    def display(self, msg='BSTMap :', order=1):
        print(msg, end='')
        if order == 1:  # 중위 순회
            self.inorder(self.root)
        elif order == 2:  # 전위 순회
            self.preorder(self.root)
        elif order == 3:  # 후위 순회
            self.postorder(self.root)
        else:
            print("잘못된 order 값입니다.")
        print()

    def search_bst(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search_bst(node.left, key)
        else:
            return self.search_bst(node.right, key)

    def search_value_bst(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_search = self.search_value_bst(node.left, value)
        return left_search if left_search is not None else self.search_value_bst(node.right, value)

    def insert_bst(self, node, new_node):
        if new_node.key < node.key:
            if node.left is None:
                node.left = new_node
            else:
                self.insert_bst(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self.insert_bst(node.right, new_node)

    def search_max_bst(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def search_min_bst(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_bst(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_bst(node.left, key)
        elif key > node.key:
            node.right = self.delete_bst(node.right, key)
        else:
            # 노드를 찾았을 때
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # 자식이 두 개인 경우
                min_larger_node = self.search_min_bst(node.right)
                node.key = min_larger_node.key
                node.value = min_larger_node.value
                node.right = self.delete_bst(node.right, min_larger_node.key)

        return node

if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value = ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ", order=1)  # 중위 순회
    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display(f"[삽입 {data[i]:2d}] : ", order=1)  # 중위 순회

    print('[최대 키] : ', map.findMax().key)
    print('[최소 키] : ', map.findMin().key)
    print('[탐색 26] : ', '성공' if map.search(26) is not None else '실패')
    print('[탐색 25] : ', '성공' if map.search(25) is not None else '실패')
    print('[탐색 일팔]:', '성공' if map.searchValue("일팔") is not None else '실패')
    print('[탐색 일칠]:', '성공' if map.searchValue("일칠") is not None else '실패')

    map.delete(3)
    map.display("[삭제  3] : ", order=1)  # 중위 순회
    map.delete(68)
    map.display("[삭제 68] : ", order=1)  # 중위 순회
    map.delete(18) 
    map.display("[삭제 18] : ", order=1)  # 중위 순회
    map.delete(35) 
    map.display("[삭제 35] : ", order=1)  # 중위 순회

    # 순회 방식에 따른 결과 출력
    print("\n순회 방식에 따른 결과:")
    map.display("[중위 순회] : ", order=1)  # 중위 순회
    map.display("[전위 순회] : ", order=2)  # 전위 순회
    map.display("[후위 순회] : ", order=3)  # 후위 순회
