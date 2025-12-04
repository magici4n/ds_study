#백준 1406번 - 링크(https://www.acmicpc.net/problem/1406)
# 1406번을 풀었지만 시간초과를 이유로 오답. 이중연결 리스트로 푸는게 나을듯.

import sys
input = sys.stdin.readline

class Node:
    def __init__(self,key,value = None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key)

class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0
        self.cursor = 0

    def pushBack(self,key):
        new_Node = Node(key)
        if self.size == 0:
            self.head = new_Node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_Node
        self.size += 1
        self.cursor += 1


    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def L(self):
        self.cursor -= 1
        if self.cursor == -1:
            self.cursor = 0
    def D(self):
        self.cursor += 1
        if self.cursor > self.size :
            self.cursor = self.size
    def B(self):
        #커서 왼쪽에 있는 문자를 삭제함.(커서가 문장의 맨 앞이면 무시됨)
        prev, v = None,self.head
        for _ in range(self.cursor -1):
            prev = v
            v = v.next

        if prev == None:
            self.head = None
        else:
            prev.next = v.next
        self.size -= 1

    def P(self,val):
        # val을 커서 왼쪽에 추가.
        new = Node(val)
        if self.cursor == 0:
            new.next = self.head
            self.head = new
        else:
            prev = self.head
            for _ in range(self.cursor - 1):
                prev = prev.next
            new.next = prev.next
            prev.next = new

        self.size += 1
        self.cursor += 1


sentence = input().rstrip()
cmd_num = int(input())
s = Singly_Linked_List()

for i in range(len(sentence)):
    s.pushBack(sentence[i])

for _ in range(cmd_num):
    cmd = input().rstrip()

    if cmd.startswith("P"):
        s.P(cmd[2:])
    elif cmd == "L":
        s.L()
    elif cmd == "D":
        s.D()
    elif cmd == "B":
        if s.cursor == 0:
            pass
        else:
            s.B()
out = []
v = s.head
while v:
    out.append(v.key)
    v = v.next
print(" ".join(out))