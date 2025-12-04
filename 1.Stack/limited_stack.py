class limited_stack:       #스택의 크기를 max_size로 정한 경우
    def __init__(self,max_size = 8):
        self.items = [None] * max_size  #max_size 크기의 리스트 선언
        self.idx = -1                   #stack의 top index

    def push(self,val):
        if self.idx+1 >= len(self.items):     #stack이 가득차 있을 때
            print("Stack is full")
            return
        self.idx += 1
        self.items[self.idx] = val

    def pop(self):
        if self.idx == -1:              #empty stack
            print("Stack is Empty")
            return None
        top_item = self.items[self.idx]
        self.idx -= 1
        return top_item

    def top(self):
        if self.idx == -1:
            print("Stack is Empty")
            return None
        return self.items[self.idx]
    def __len__(self):
        return self.idx+1

    def isEmpty(self):
        return len(self) == 0