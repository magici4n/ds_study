#백준 10828번- 링크(https://www.acmicpc.net/problem/10828)
#문제내에 실행시간 제약이 있어서 리스트로 한번에 출력함.
class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)
    def pop(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return -1
    def top(self):
        if self.size() > 0:
            return self.items[-1]
        else :
            return -1
    def size(self):
        return len(self.items)
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

N = int(input())
result = []
S = Stack()
for _ in range(N):
    cmd = input()
    if cmd.startswith("push"):
        S.push(cmd[5:])
    elif cmd == "top":
        result.append(S.top())
    elif cmd == "size":
        result.append(S.size())
    elif cmd == "pop":
        result.append(S.pop())
    else :
        result.append(S.empty())

for i in range(len(result)):
    print(result[i])