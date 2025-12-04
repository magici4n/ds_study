#백준 10845번 - 링크(https://www.acmicpc.net/problem/10845)
class Queue :
    def __init__(self):
        self.items = []
        self.front_index = 0

    def push(self,val):
        self.items.append(val)
    def pop(self):
        if self.front_index == len(self.items):
            return -1
        else:
            X = self.items[self.front_index]
            self.front_index += 1
            return X
    def size(self):
        return len(self.items) - self.front_index
    def empty(self):
        if self.front_index == len(self.items):
            return 1
        else : return 0
    def front(self):
        if self.front_index == len(self.items):
            return -1
        else:
            return self.items[self.front_index]
    def back(self):
        if self.front_index == len(self.items):
            return -1
        else:
            return self.items[-1]

q = Queue()
N = int(input())
result = []
for _ in range(N):
    cmd = input()
    if cmd.startswith("push"):
        q.push(int(cmd[5:]))
    elif cmd == "pop":
        result.append(q.pop())
    elif cmd == "size":
        result.append(q.size())
    elif cmd == "empty":
        result.append(q.empty())
    elif cmd == "front":
        result.append(q.front())
    else:
        result.append(q.back())

for i in range(len(result)):
    print(result[i])