class Node():
    def __init__(self,key,value = None):
        self.key = key
        self.value = value
        self.prev = self.next = self

    def __str__(self):
        return str(self.key)
class Doubly_Linked_List():
    def __init__(self):
        self.head = Node()
        self.size = 0
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return "->".join(str(v) for v in self)
    def __len__(self):
        return self.size

    def splice(self,a : Node, b : Node, x : Node):
        ap = a.prev
        bn = b.next
        xn = x.next

        ap.next = bn
        bn.prev = ap

        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b

    def search(self,key):
        v = self.head.next
        while v != self.head :
            if v.key == key:
                return v
            v = v.next
        return None

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            return None
        return self.head.next
    def last(self):
        if self.isEmpty():
            return None
        return self.head.prev

    def moveAfter(self,a,x):                #a를 노드 x뒤로 이동
        self.splice(a,a,x)
    def moveBefore(self,a,x):               #a를 노드 x앞으로 이동
        self.splice(a,a,x.prev)
    def insertAfter(self,x,key):            #노드 x뒤에 데이터가 key인 새 노드를 생성해 삽입
        self.moveAfter(Node(key),x)
        self.size +=1
    def insertBefore(self,x,key):           #노드 x앞에 데이터가 key인 새 노드를 생성해 삽입
        self.moveBefore(Node(key),x)
        self.size += 1
    def pushFront(self,key):
        self.insertAfter(self.head,key)

    def pushBack(self,key):
        self.insertBefore(self.head,key)

    def popFront(self):
        v = self.head.next
        key = v.key
        self.head.next = v.next
        v.next.prev = self.head
        del v
        self.size -= 1
        return key
    def popBack(self):
        v = self.head.prev
        key = v.key
        self.head.prev = v.prev
        v.prev.next = self.head
        del v
        self.size -= 1
        return key

    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1