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

# 처음 풀이
n = int(input())
s = Stack()
input_lst = []
result_lst = []
current_num = 1
for _ in range(n):
    input_lst.append(int(input()))

for num in input_lst:
    while True:
        if s.isEmpty():
                s.push(current_num)
                current_num += 1
                result_lst.append('+')
        elif s.top() < num:
            s.push(current_num)
            current_num += 1
            result_lst.append('+')
        else:
            s.pop()
            result_lst.append('-')
            break

if not s.isEmpty():
    print("NO")
else:
    for num in result_lst:
        print(num)
"""
# 개선된 풀이
n = int(input())
s = Stack()
input_lst = [int(input()) for _ in range(n)]
result = []
current = 1

for num in input_lst:
    while current <= num:
        s.push(current)
        result.append('+')
        current += 1

    if s.top() == num:
            s.pop()
            result.append('-')
    else :
        print("NO")
        exit()

for ch in result:
    print(ch)
"""