class Node:
    def __init__(self, key = None, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
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

class BST :
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __str__(self):      # 한 방향 리스트 __str__과 유사
        return " - ".join(str(k) for k in self)

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None            # v의 부모
        v = self.root
        while v :           # while v != None
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key :     # key is in tree
            return p
        else :                      # key is not in tree
            return None

    def insert(self, key):          # value값도 추가로 받을 수 있음.
        p = self.find_loc(key)

        if p == None or p.key != key :      # tree안에 key값이 없어야 삽입하니깐 체크
            v = Node(key)                   # 삽입 노드 생성
            if p == None:                   # 트리가 빈 트리라면
                self.root = v               # 삽입할 노드를 루트로

            else :
                v.parent = p                # p가 삽입될 곳의 부모노드기 때문.

                if p.key >= key :           # 왼쪽에 넣을지 오른쪽에 넣을지
                    p.left = v
                else :
                    p.right = v

            self.size += 1

            # 이 곳에 height 정보 update하는 코드 또는 함수 삽입
            # update_height 함수를 준비해 호출하는 식으로(밑의 코드)
            return v
        else :
            print("key is already in tree")
            return p                            # 중복 key를 허용하지 않으면 None 리턴


    def update_node_height(self, v):            # 노드 v의 높이 수정
        if v :
            l = v.left.height if v.left else -1
            r = v.right.height if v.right else -1
            v.height = max(l, r) + 1

    def update_height(self, v):         # v에서 root까지 올라가면서 높이 수정
        while v != None:
            self.update_node_height(v)
            v = v.parent


    def deleteByMerging(self,x):
        # assume that x is not None
        a, b, pt = x.left, x.right, x.parent
        # c = node which will be at the position x
        # s = 균형이 깨질 가능성이 있는 첫 번째 노드를  리턴함
        # -> 균형 이진 탐색 트리의 delete 연산에 이용될 예정

        if a == None :
            c = b
            s = pt
        else :                      #a != None
            c = m = a
            while m.right :         # find m
                m = m.right

            # make b as the right child of m
            m.right = b
            if b :
                b.parent = m
            s = m

        # 여기까지는 a가 비었을때 아닐 때
        # 밑에는 지우는 노드가 루트일 때 아닐때

        if self.root == x :     # c becomes a new root
            if c:
                c.parent = None
            self.root = c

        else:                   # c becomes a child of pt (of x)
            if pt.left == x:    # 이걸 체크하는 이유? 삭제할 노드 x가 왼쪽 자식인지 오른쪽 자식인지 확인
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1

        self.update_height(s)  # s부터 root까지 높이 수정

        return s                    # first node that would be rebalanced

