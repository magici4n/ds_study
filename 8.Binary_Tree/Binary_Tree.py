class Node:
    def __init__(self, key = None, parent = None, left = None, right = None):
        self.key = key
        # self.value = value       필요시 추가 / 부가 정보
        # self.height = height     필요시 추가 / 노드의 높이
        self.parent = parent
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.key)

    def preorder(self):
        if self != None:
            print(self.key)
            if self.left : self.left.preorder()
            if self.right : self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left : self.left.inorder()
            print(self.key)
            if self.right : self.right.inorder()

    def postorder(self):
        if self != None:
            if self.left : self.left.postorder()
            if self.right : self.right.postorder()
            print(self.key)
