#백준 2504번 - 링크(https://www.acmicpc.net/problem/2504)
"""
# 풀다가 못 품
class Stack :
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]
    def __len__(self):
        return len(self.items)

par = input()
s= Stack()
flag = 0
total_point = 0
cur_point = 0
for ch in par :
    if s.isEmpty():
        cur_point = 0

    if ch == '(':

    elif ch == '[':

    elif ch == ')':

    elif ch == ']':

    else :



"""