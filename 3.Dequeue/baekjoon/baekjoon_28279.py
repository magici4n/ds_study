#백준 28279번 - 링크(https://www.acmicpc.net/problem/28279)

class Deque:
    def __init__(self):
        self.items = []
    def append(self,val):
        self.items.append(val)
    def append_left(self,val):
        self.items.insert(0,val)
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.items.pop()
    def pop_left(self):
        if self.isEmpty():
            return -1
        else:
            return self.items.pop(0)
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        if len(self) == 0:
            return 1
        else:
            return 0
    def peek_front(self):
        if self.isEmpty():
            return -1
        else:
            return self.items[0]
    def peek_back(self):
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

d = Deque()
N = int(input())
result = []
for _ in range(N):
    cmd = input()
    if cmd.startswith("1"):
        d.append_left(int(cmd[2:]))
    elif cmd.startswith("2"):
        d.append(int(cmd[2:]))
    elif cmd == "3":
        result.append(d.pop_left())
    elif cmd == "4":
        result.append(d.pop())
    elif cmd == "5":
        result.append(len(d))
    elif cmd == "6":
        result.append(d.isEmpty())
    elif cmd == "7":
        result.append(d.peek_front())
    else :
        result.append(d.peek_back())

for i in range(len(result)):
    print(result[i])