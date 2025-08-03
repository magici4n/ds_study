#백준 1874번 - 링크(https://www.acmicpc.net/problem/1874)

class Stack():
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if self.isEmpty():
            return None
        else :
            return self.items.pop()
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0

n = int(input())
s = Stack()

