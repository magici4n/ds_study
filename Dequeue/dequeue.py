class Dequeue:
    def __init__(self):
        self.items = []
    def append(self,val):
        self.items.append(val)
    def append_left(self,val):
        self.items.insert(0,val)        #O(n)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
    def pop_left(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)                #O(n)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def peek_front(self):
        """왼쪽(앞) 값 확인"""
        if self.isEmpty():
            return None
        return self.items[0]

    def peek_back(self):
        """오른쪽(뒤) 값 확인"""
        if self.isEmpty():
            return None
        return self.items[-1]