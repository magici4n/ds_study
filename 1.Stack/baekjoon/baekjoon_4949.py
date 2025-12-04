#백준 4949번 - 링크(https://www.acmicpc.net/problem/4949)
class Stack():
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
        return len(self) == 0

    def top(self):
        if len(self)== 0:
            return None
        else:
            return self.items[-1]

    def __len__(self):
        return len(self.items)

while True:
    flag = 0
    sentence = input()
    s = Stack()

    if sentence ==".":
        break

    for ex in sentence:
        test = ' '
        if ex == '(':           # ( 가 들어오면
            s.push('(')
        elif ex == '[':         # [ 가 들어오면
            s.push('[')
        elif ex == ')':         # ) 가 들어오면
            while test != '(':   # ( 가 pop될때까지
                if s.isEmpty():
                    flag = 1
                    break
                test = s.pop()
                if test == '[':
                   flag = 1
                   break
        elif ex == ']':         # ] 가 들어오면
            while test != '[':  # [ 가 pop 될때까지
                if s.isEmpty():
                    flag = 1
                    break
                test = s.pop()
                if test == '(':
                    flag = 1
                    break
        else:
            pass
    if not s.isEmpty():
        print("no")
    elif flag == 1:
        print("no")
    else:
        print("yes")

"""
#gpt가 리팩토링 해준 버전
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

while True:
    flag = 0
    sentence = input()
    if sentence == ".":
        break

    s = Stack()

    for ch in sentence:
        if ch == '(' or ch == '[':
            s.push(ch)
        elif ch == ')':
            if s.isEmpty() or s.pop() != '(':
                flag = 1
                break
        elif ch == ']':
            if s.isEmpty() or s.pop() != '[':
                flag = 1
                break

    if not s.isEmpty():
        flag = 1

    print("no" if flag else "yes")

"""