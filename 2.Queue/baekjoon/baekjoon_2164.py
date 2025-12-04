# 백준 2164번 - 링크(https://www.acmicpc.net/problem/2164)

class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if self.front_index == len(self.items):
            return None
        else:
            X = self.items[self.front_index]
            self.front_index += 1
            return X
    def front(self):
        return self.items[self.front_index]

    def __len__(self):
        return len(self.items)- self.front_index

q = Queue()
N = int(input())

for i in range(1,N+1):
    q.enqueue(i)

while len(q) != 1:
    q.dequeue()
    q.enqueue(q.dequeue())

print(q.front())
