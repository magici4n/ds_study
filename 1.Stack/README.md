## Stack
_____________________________________________________
- LIFO구조 (Last in First Out)
- 주요 연산 **push**, **pop**, **top**, **isEmpty**, **size(len)**
- 데이터는 파이썬 리스트에 저장(append, pop이 제공되므로)

**아래 코드는 stack.py와 동일**
<pre>
<code>
class Stack:
    def __init__(self):
        self.items = []             #데이터 저장을 위한 리스트 준비

    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:                        #pop할 아이템이 있으면
            self.items.pop()        #(try except대신에)
                                    #(isEmpty로 조건식 가능)
        except IndexError:          #없으면 IndexError
            print("Stack is Empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):              #len()로 호출하면 stack의 item 수 반환
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0
</code>
</pre>

- 위에서 정의한 Stack클래스는 파이썬의 리스트 자료구조를 그대로 사용한 경우이다.
  따라서 **push(append)**, **pop** 은 모두 평균 **O(1)**시간을 보장한다.
- 그러나 파이썬의 리스트는 동적 배열이기 때문에 크기를 자동으로 조절하면서 메모리 관리를 할 때
  최악의 경우 상수시간을 보장 못한다.
- 따라서 최악의 경우에도 상수시간을 보장하려면 미리 스택의 크기를 할당해야한다.

## 스택의 크기가 정해져 있는 경우
**추가 사항** 
* push 연산에서 빈공간이 있는지 확인해야함.
* 스택에 가장 최근에 저장된 값을 알기 위한 변수가 필요(idx)
* append,pop를 사용 안하기 위해서 고정 크기의 리스트를 미리선언
  -> append사용시 리스트는 동적 배열이기 때문에 상수시간 보장 불가 ->**limited_stack.py에서 참고바람**

## 스택의 연산시간
- push() : O(1)
- pop() : O(1)
- top() : O(1)
- isEmpty() : O(1)


## 결론
-스택은 연산은 대부분 O(1)으로 빠름(단 재할당시 예외) 
-순차적 탐색이 불편하며(top 외에는 전부 꺼내야 탐색가능),
 중간요소에 접근이 불가, 앞 요소를 꺼내야하는 구조에는 부적합


## 스택 사용 예시

**1. 괄호 맞추기**
- parChecker.py 참고

**2. infix 수식을 postfix 수식으로 전환**
- infix_to_postfix.py 참고

**3. postfix수식을 실제로 계산하기**
- postfix_cal.py 참고 (한 자리수 계산만 가능)
  
**4. Nearest smaller element 계산하기**

**백준 예제 풀어보기**
- 초급 - 스텍 기본 개념 
1. 10828 ->baekjoon_10828 참고
2. 9012  ->baekjoon_9012 참고
3. 10773 ->baekjoon_10773 참고
4. 1874  ->baekjoon_1874 참고
5. 4949  ->baekjoon_4949 참고 
- 중급 - 응용 + 알고리즘 사고 키우기
1. 2504 ->
2. 2493 ->
3. 5397 ->
4. 17298 ->

- 도전과제
1. 6549 ->
2. 2812 ->




