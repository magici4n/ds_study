#백준 10866번 - 링크(https://www.acmicpc.net/problem/10866)

class Deque:
    def __init__(self):
        self.items = []

    def push_front(self,val):
        self.items.insert(0,val)
    def push_back(self,val):
        self.items.append(val)
    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.items.pop(0)
    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def front(self):
        if self.empty():
            return -1
        else:
            return self.items[0]
    def back(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]

d = Deque()
N = int(input())
result = []

for _ in range(N):
    cmd = input()

    if cmd.startswith("push"):
        if cmd[5] == "b":
            d.push_back(int(cmd[10:]))
        else:
            d.push_front(int(cmd[11:]))
    elif cmd.startswith("pop"):
        if cmd[4] =="b":
            result.append(d.pop_back())
        else:
            result.append(d.pop_front())
    elif cmd == "size":
        result.append(d.size())
    elif cmd == "empty":
        result.append(d.empty())
    elif cmd == "front":
        result.append(d.front())
    else:
        result.append(d.back())

for i in range(len(result)):
    print(result[i])