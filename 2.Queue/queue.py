class queue:
    def __init__(self):
        self.items = []         #데이터 저장을 위한 리스트
        self.front_index = 0    #다음 dequeue될 index
    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items): #왜 이렇게 하는지 고민해보기
            print("Q is empty")
            return None
        else:
            X = self.items[self.front_index]
            self.front_index +=1
            return X
    def front(self):
        if self.front_index == len(self.items):
            print("Q is empty")
            return None
        else:
            return self.items[self.front_index]