#백준 9012번- 링크(https://www.acmicpc.net/problem/9012)
#문제 자체는 스택을 안 써도 되긴함.
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
    def __len__(self):
        return len(self.items)

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]
    def isEmpty(self):
        return len(self)==0


def check_vps(vps : str):
    s = Stack()
    for token in vps:
        if token == '(':
            s.push(token)
        else :
            if len(s) == 0:
                return print("NO")
            else:
                s.pop()
    if len(s) >0:
        print("NO")
    else :
        print("YES")
N = int(input())
for _ in range(N):
    vps = input()
    check_vps(vps)


