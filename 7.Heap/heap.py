class Heap:
    def __init__(self, L = []):
        self.A = L
        self.make_heap()
    def __str__(self):
        return str(self.A)

    def heapify_down(self,k,n):
        while 2 * k + 1 < n:         #리프 노드가 아니면 반복
            L, R = 2 * k + 1, 2 * k +2      #L은 왼쪽 자식노드, R은 오른쪽 자식노드
            if self.A[L] > self.A[k]:       #세 노드의 최대값의 인덱스 찾기/ m은 max의미
                m = L
            else:
                m = k

            if R < n and self.A[R] > self.A[m]:
                m = R
            # m = A[k], A[L], A[R] 중 최대값의인덱스
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k,n)
    def heapify_up(self,k):             # 올라가면서 A[k]를 재 배치
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[(k-1)//2], self.A[k] = self.A[k], self.A[(k-1)//2]
            k = (k-1)//2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)
    def find_max(self):
        return self.A[0]
    def delete_max(self):
        if len(self.A) == 0 :
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapify_down(0,len(self.A))
        return key

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1,-1,-1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n-1
            self.heapify_down(0,n)