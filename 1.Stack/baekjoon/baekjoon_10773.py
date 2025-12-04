#백준 10773번 - 링크(https://www.acmicpc.net/problem/10773)
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
    def isEmpty(self):
        return len(self.items) == 0

K = int(input())
s = Stack()
sum = 0
for _ in range(K):
    val = int(input())
    if val == 0:
        sum -= s.pop()
    else:
        s.push(val)
        sum += val
print(sum)

"""
이렇게 짧게도 가능
K = int(input())

nums = []
sum = 0

for _ in range(K):
    N = int(input())

    if N == 0:
        sum -= nums.pop()

    else :
        nums.append(N)
        sum += N
print(sum)
"""
