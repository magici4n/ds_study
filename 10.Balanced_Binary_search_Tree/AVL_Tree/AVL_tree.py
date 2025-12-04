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



class AVL(BST):         #BST 클래스를 부모 클래스로 지정
    # BST 클래스의 멤버, 메소드 상속받아 사용가능
    # __init__가 없으므로 부모 클래스 __init__가 자동 호출된다.
    def rotationRight(self, z):  # rotationLeft도 유사하게 정의
        if z == None: return  # z가 None일 때 do nothing
        x = z.left
        if x == None: return  # x가 None일 때 no rotate
        b = x.right  # b가 None인 경우는 상관 없음

        # 이제부터 rotate
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:  # z의 위치찾기
                z.parent.left = x
            else:
                z.parent.right = x

        x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z

        # z가 루트였다면 x가 새로운 루트가 되어야함.
        if z == self.root:
            self.root = x

        # height를 관리한다면 z와 x의 height 수정하는 코드 추가해야함.
        self.update_node_height(z)
        self.update_node_height(x)

    def rotationLeft(self, z):
        if z == None: return
        x = z.right
        if x == None: return
        a = x.left

        # 이제부터 rotate
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x

        x.left = z
        z.parent = x
        z.right = a
        if a:
            a.parent = z

        # z가 루트였다면 x가 새로운 루트노드
        if z == self.root:
            self.root = x
        # height를 관리한다면 z와 x의 height 수정하는 코드 추가해야함.
        self.update_node_height(z)
        self.update_node_height(x)

    def rebalance(self, x, y, z):
        if z == None:           #rebalance 불필요
            return

        if z.left == y and y.left == x:     # 왼쪽 방향 일직선
            self.rotationRight(z)
            return y
        elif z.right == y and y.right == x:     # 오른쪽 방향 일직선
            self.rotationLeft(z)
            return y
        elif z.left == y and y.right == x:      # 삼각형 경우 1
            self.rotationLeft(y)
            self.rotationRight(z)
            return x
        else:                                   # 삼각형 경우 2
            self.rotationRight(y)
            self.rotationLeft(z)
            return x



    def insert(self,key):
        # BST의 insert함수는 실제 삽입된 노드가 리턴됨.

        v = super(AVL,self).insert(key)

        #2. find x, y, z  ->   조상노드를 따라가면서 찾기
        x, y, z = v, v.parent, None
        while y:
            z = y.parent
            if z and abs(z.left.height - z.right.height) <= 1:
                 x, y = y, z
            else:
                   break
        w = self.rebalance(x, y, z)
        if w.parent == None:    # root가 바뀐 경우
            self.root = w

    def delete(self, u):
        # deleteByMerging, Copying 둘 다 가능
        # 노드의 삭제로 노드 높이에 영향을 받는 (불균형 가능성 있는)
        # 첫 노드가 리턴된다 가정
        s = super(AVL, self).deleteByMerging(u)

        while s != None:            #go up to root
            # update s.height properly
            if abs(s.right.height - s.left.height) > 1 :       # z - y - x chain 존재
                z = s
                # z.left, z.right가 None인 경우에 height - 1 로 가정
                if z.left.height >= z.right.height:
                    y = z.left
                else:
                    y = z.right
                if y.left.height >= y.right.height :
                    x = y.left
                else:
                    x = y.right
                s = self.rebalnce(x, y, z)
                # rebalance는 rotation 후 새로운 top 노드를 리턴
            w = s
            s = s.parent
            self.root = w       # w 가 새로운 루트 노드가 될 수 있음.







