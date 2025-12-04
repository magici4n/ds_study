# 백준 1158번 - 링크(https://www.acmicpc.net/problem/1158)


class Node():
    def __init__(self,key):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)
class singly_linked_list():
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def pushFront(self,key):
        v = Node(key)
        v.next = self.head
        self.head = v
        self.size += 1

    def pushBack(self,key):
        v = Node(key)
        if self.size == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size += 1

    def popFront(self):
        if self.size == 0 :
            return
        else:
            x = self.head
            key = x.key
            self.head = x.next
            del x
            self.size -= 1
        return key

    def popBack(self):
        if self.size == 0:
            return
        else:
            prev,tail = None,self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key
    def remove(self,v):
        if self.size == 0 or v == None:
            return
        elif self.head == v:
            self.popFront()
        else:
            w = self.head
            while w.next != v:
                w = w.next
            w.next = v.next
            self.size -= 1


def Josephus(n,k):
    s = singly_linked_list()

    result = []

    for x in range(1,n+1):          #리스트 채우기
        s.pushBack(x)
    rmv = s.head

    for _ in range(len(s)-1):       #원형 리스트 만들기
        rmv = rmv.next
    prev = rmv

    rmv.next = s.head
    rmv = rmv.next
    for _ in range(n):
        for _ in range(k-1):
            prev = rmv
            rmv = rmv.next
        result.append(rmv.key)
        prev.next = rmv.next
        rmv = prev.next

    print("<" + ", ".join(map(str, result)) + ">")
N,K = map(int,input().split())
Josephus(N,K)
