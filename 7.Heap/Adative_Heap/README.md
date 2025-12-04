## 적응형 힙(Adative Heap)
_________________________________________________________
앞에서 살펴본 힙 제공 연산은 *delete_max, insert, heap_sort 등이다.   
만약 특정 key 값을 삭제하거나,변경하려면 어떻게 해야할까?    

**새로운 두 연산이 필요하다**    
1. remove(key) : key 값을 힙으로부터 제거
2. update_key(old_key, new_key)  : old_key값을 new_key값으로 대체
    1. old_key < new_key 라면 heapify_down 호출 필요
    2. old_key > new_key 라면 heapify_up 호출 필요


**발생하는 문제**   
1. remove(key)를 수행하기 위해선, 힙에서 key 값이 저장된 위치(index)를 알아야함.   
2. update_key(old_key, new_key)를 수행하기 위해선, old_key의 값이 저장된 힙의 index를 알아야 한다.   

-> 각 key 값이 저장된 위치(index)를 기억하고 있도록 하자

**Locator 클래스**    
key 값과 key 값이 저장된 index를 쌍으로 담는 클래스 선언    
-> 각 key 값은 하나의 Locator 객체에 value,index 값과 함께 담겨 힙에 저장된다.

<pre>
<code>
class Locator:
    def __init__(self, key, value, j):
        self.key = key      # key값
        self.value = value  # value값 (optional)
        self.index = j      # key 값이 저장된 index j
</code>
</pre>


**AdaptedHeap 클래스**   
Locator 객체가 저장되는 힙 리스트 A가 필요하고,    
각 key 값이 담긴 Locator 객체를 연결하는 사전(dict) D도 필요하다.

<pre>
<code>
# Locator 클래스를 여기서 선언 (클래스 안에 다른 클래스 선언 가능)
def __init__(self):
   self.A = []    # 여기선 빈 리스트로 초기화
   self.D = {}    # dict : D[key] = locator

def __str__(self):
   return str(self.A)

def __len__(self):
   return len(self.A)

def find_loc(self,key):      # return Locator obj. of key
   return self.D.get(key)    # None if key is not in D 

def insert(self, key, value = None):
   loc = self.Locator(key, value, len(self.A))
      # 마지막에 (key, index) Locator 객체 삽입
   self.A.append(loc)   #힙 리스트에 loc 삽입됨!
   self.heapify_up(loc.index)
   self.D[key] = loc    #key 값에 대한 Locator 객체 링크 저장
   return loc

def heapify_up(self, i):      # 인덱스 i 에 저장된 item을 up
   p = (i - 1)//2
   if p > 0 and self[p].key < self.A[i].key:
      #key swap
      self.A[i].key, self.A[p].key = self.A[p].key, self.A[i].key
      #index swap
      self.A[i].index = i
      self.A[p].index = k
      heapify_up(p)

def heapify_down(self, i):
   # heapify_up과 유사하게 작성가능 한 번 해보자

def remove(self, loc):      # key 값이  아닌 Locator객체가 전달됨
   k = loc.index            # self.A[k]에 있는 item을 지우면됨!
   
   if not (0 <= k < len(self) and self.A[k] == loc):
      # loc이 힙에 저장된 것이 아니라면 error
      raise ValueError('Invalid locator')
      
       # 1. A[k]와 A[-1]을 swap!
      swap self.A[k] and self.A[-1]
      swap indices of A[k] and A[-1]
       # 2. A[-1]을 pop!
      self.A.pop()
       # 3. A[k]를 heapify_down해서 재 배치
      self.heapify_down(k)

      del self.D[key]      # dict D에서(key, loc) 제거

def find_max(self):        # return a tuple (max_key, max_value)
      max_key = max_val = None
      if len(self) > 0:
         max_loc = self.A[0]
         max_key, max_val = self.A[0].key, self.A[0].value
         self.remove(max_loc)
      return max_key, max_val

def update_key(self, loc, new_key):
      # loc.index에 저장된 key 값을 new_key 값으로 대체
      old_key = loc.key
      
      k = loc.index
      if not (0 <= k < len(self) and self.A[k] == loc):
         # loc이 힙에 저장된 게 아니라면 error
         raise ValueError('Invalied locator')
      if loc.key > new_key :        # new_key가 더 작기 때문에 down!
         loc.key = new_key
         self.heapify_down(k)
      if loc.key < new_key :        # new_key가 더 크기 때문에 up!
         loc.key = new_key
         self.heapify_up(k)
      
      #update D
      del self.D[old.key]
      self.D[new_key] = loc

   

   
</code>
</pre>

