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
    small = Stack()
    big = Stack()
    sentence = input()
    pop_lst= []
    if sentence == '.':
        break
    for ch in sentence:
        if ch == '[' :
            big.push('[')
            pop_lst.append('[')
        elif ch == ']':
            pop_lst.append(big.pop())

        elif ch == '(':
            small.push('(')
            pop_lst.append('(')
        elif ch == ')':
            pop_lst.append(small.pop())
        else :
            pass

    if len(small) == 0 and len(big) == 0:
        recent = pop_lst[0]
        for i in (1,len(pop_lst)):
            if recent == '(':
                if pop_lst[i] == ']':
                    print("no")
                    break
                else:
                    recent = pop_lst[i]

            elif recent == '[':
                if pop_lst[i] == ')':
                    print("no")
                    break
                else:
                    recent = pop_lst[i]
            else:
                recent = pop_lst[i]
                pass
    else:
        print("no")