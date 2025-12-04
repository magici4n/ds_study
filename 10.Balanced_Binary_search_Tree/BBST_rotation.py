def rotationRight(self, z):         # rotationLeft도 유사하게 정의
    if z == None: return            # z가 None일 때 do nothing
    x = z.left
    if x == None : return           # x가 None일 때 no rotate
    b = x.right                     # b가 None인 경우는 상관 없음

    #이제부터 rotate
    x.parent = z.parent
    if z.parent:
        if z.parent.left == z:      # z의 위치찾기
            z.parent.left = x
        else :
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
    # self.update_node_height(z)
    # self.update_node_height(x)

def rotationLeft(self, z):
    if z == None: return
    x = z.right
    if x == None: return
    a = x.left

    # 이제부터 rotate
    x.parent = z.parent
    if z.parent :
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
    # self.update_node_height(z)
    # self.update_node_height(x)